import os
import time
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.BOPAlgo import BOPAlgo_MakeConnected
from OCC.Core.BRepTools import breptools

def import_step_file(filename):
    """Import a STEP file and return the shape."""
    reader = STEPControl_Reader()
    status = reader.ReadFile(filename)
    if status != 1:
        raise ValueError(f"Error reading STEP file: {filename}")
    reader.TransferRoot()
    shape = reader.Shape()
    return shape

def export_to_brep(shape, filename):
    """Export a TopoDS_Shape to a BREP file."""
    breptools.Write(shape, filename)

def main(num_threads):
    # Set the number of OpenMP threads
    os.environ["OMP_NUM_THREADS"] = str(num_threads)
    
    # Import the STEP files
    surface_shape = import_step_file("last_dura.step")
    volume_shape = import_step_file("last_diff.step")
    
    # Perform the fuse operation
    fuse_algo = BRepAlgoAPI_Fuse(volume_shape, surface_shape)
    fuse_algo.Build()
    
    # Use BOPAlgo_MakeConnected to ensure the mesh is connected
    mk_connected = BOPAlgo_MakeConnected()
    mk_connected.AddArgument(fuse_algo.Shape())
    mk_connected.SetRunParallel(True)
    
    # Measure the execution time
    start_time = time.time()
    mk_connected.Perform()
    end_time = time.time()
    
    connected_shape = mk_connected.Shape()

    # Export the connected shape to a BREP file
    brep_filename = f"connected_shape_{num_threads}.brep"
    export_to_brep(connected_shape, brep_filename)
    print(f"Connected shape exported to {brep_filename}")
    print(f"Total execution time with {num_threads} threads: {end_time - start_time:.9f} seconds")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <num_threads>")
        sys.exit(1)
    num_threads = int(sys.argv[1])
    main(num_threads)
