# QM/MM RE-EDS
An efficient multistate multiscale free-energy method.

## Publications

- Preprint on [arXiv]()

## Abstract
Calculating free-energy differences using molecular dynamics (MD) simulations is an important task in computational chemistry. In practice, the accuracy of the results is limited by the model approximations and insufficient phase-space sampling due to limited computational resources. In the present work, we address these challenges by integrating the quantum-mechanical/molecular-mechanical (QM/MM) scheme with replica-exchange enveloping distribution sampling (RE-EDS) to obtain a multistate and multiscale free-energy method with high computational efficiency. The performance of QM/MM RE-EDS is showcased by calculating hydration free energies for three datasets using semi-empirical methods for the QM zone. We highlight the importance of the choice of QM Hamiltonian and the effect of the compatibility between the QM and MM models. Especially the choice of semi-empirical method has a substantial effect on the accuracy compared to experiment, but also the choice of MM water model is non-negligible. Our findings indicate that RE-EDS is an efficient approach for calculating free-energy differences with a QM/MM scheme, and lays the foundation for future developments and applications.

## Description

This repository contains input files required to reproduce this work in the input_files folder and an examlple analysis in the analysis folder.

A GROMOS version with QM/MM RE-EDS implementation is available [here](https://github.com/rinikerlab/gromosXX) (check out branch: `alchemical_eds`).

# Author

Domen Pregeljc ([@dpregeljc](https://github.com/dpregeljc))
