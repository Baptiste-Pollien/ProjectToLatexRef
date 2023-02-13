#!/bin/bash

# Run the script
python3 ../projectToLatexRef.py ./project_refs.json

# Builf the latex file
latexmk -lualatex -pdf main.tex