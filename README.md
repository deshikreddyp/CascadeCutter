# CascadeCutter
# OpenCascade Boolean Operations

This repository demonstrates how to perform and parallelize boolean operations using OpenCascade, specifically focusing on generating conformal volumes by embedding a surface within a volume.

## Overview

Boolean operations in OpenCascade can be used to combine or manipulate shapes. This repository covers:
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

## Structure
OpenCascade_Boolean_Operations/
│
├── boolean_operations.py
├── README.md
