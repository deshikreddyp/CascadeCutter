# CascadeCutter

Small Python utility for fusing two STEP geometries with OpenCascade and exporting a connected BREP result. The workflow is intended for geometry preparation where a conformal interface is needed before downstream meshing, including fluid-structure-interaction workflows.

## Requirements

- Python 3
- PythonOCC bindings that provide the `OCC` module
- Two STEP files: `last_dura.step` and `last_diff.step`

## Run

Place the two input STEP files beside `boolean_fuse.py`, then run:

```bash
python boolean_fuse.py <num_threads>
```

For example:

```bash
python boolean_fuse.py 4
```

The script reads the two STEP files, performs a Boolean fuse, runs `BOPAlgo_MakeConnected` with parallel processing enabled, and writes `connected_shape_<num_threads>.brep`.

## Scope

This is a focused geometry-preparation utility. It does not generate a mesh or include the input geometries; users provide their own compatible STEP files.
