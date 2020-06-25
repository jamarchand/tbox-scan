#!/bin/bash
#Initialize T-box predictions pipeline

#echo "Installing dependencies"
#conda init bash
#conda env create -f environment.yml
#source activate tbdb



python3 setup.py sdist bdist_wheel

python3 -m twine upload --repository testpypi dist/*
#exec bash
