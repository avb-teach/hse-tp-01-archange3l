#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: ./collect_files.sh input_dir output_dir [--max_depth N]"
    exit 1
fi

if grep -qi "mingw" <<< "$(uname -a)"; then
    PYTHON_CMD="winpty python"
else
    PYTHON_CMD="python3"
fi

$PYTHON_CMD collect_files.py "$@"
