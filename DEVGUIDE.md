# Developer Guidelines

Hi there ! In this document, we'll cover all the different guidelines, 
recommandations, and best practices we want you to keep in mind while 
contributing to the bdacore project. This document must be kept up-to-date with
the current team views and opinions, and not taken as a frozen set of 
immutable rules.

## Overview
* Build and install from local, and test
* Organisation & Packaging
###TODO
* Absolute vs Relative imports
* Docstrings
* Methods ordering

## Build and install from local

We use [conda](https://conda.io/docs/) to work on bdacore and manage virtual environments.

#### virtualenv

    make develop_env

It creates a new conda environment and adds 
requirements listed in the requirements.txt file plus dev_requirements.txt.
    
#### install from local folder

The best way to install ddapi from a local git repository is to use setuptools' develop installation
mode. There is a shortcut for that in the Makefile :
    
    make develop

It creates a symlink in the site-packages folder of the python associated wtih the virtualenv.

#### run tests

Run tests and show actual coverage. The Jenkinsfile is used by Jenkins (Build Factory) and defines the coverage value
you can't be below

    make unittests
    
    make acceptance-tests
  

#### compile 
 
The following commands will pull dependencies from the meta.yaml file, and then build the sources.

    make dist   
    
It creates 2 archive files in the current folder

ex :

    ./dist/bdacore-X.X.X.dev0.tar.tgz
    ./dist/bdacore-X.X.X.dev0-py2-none-any.whl


## Organisation & Packaging

We follow these principles : [python packaging](https://blog.ionelmc.ro/presentations/packaging/#slide:1)

Very Important Files : 

 * **setup.py** file contains the current version of the package.
 We use [zest-releazer](http://zestreleaser.readthedocs.io/en/latest/overview.html) 
 to release and to version every artifacts of DD's project 
 * **MANIFEST.in** file lists the 'non python files' to be included 
 in the archive package by setuptools
 * **Makefile** file contains targets about the life cycle of the project 
 (test, install, dist, develop, etc..)
 * **ci/Jenkinsfile** file defines the pipeline used by Jenkins to build, to test, and to push artifacts
    * each git branch has its own build (see [Jenkins' Multibranch pipeline feature](https://jenkins.io/doc/tutorials/build-a-multibranch-pipeline-project/))
    * each build pushes the final artifact to [anaconda.org](https://anaconda.org/octo/dashboard) 
    with **the label set to the branch's name** (see [Anaconda's label feature](https://docs.anaconda.com/anaconda-cloud/user-guide/tutorials))
 * **setup.cfg** file lists all packages to install with pyddapi to run correctly
    * if you want to add a new package, please verify if there is a binary version on PYPI
    (bdist_wheel / any_wheel). If no, add the conda package installation instead in the Makfile
    into the **env target** and/or in the **develop target**
    * ***you should never add GCC or any compilation dependency*** to facilitate installation 
 * **ci/test_requirements.txt** file lists only packages required for development purpose (testing, coverage, linter, etc...)
 * **ci/Dockerfile** file is used by Jenkins to build bdacore inside a docker container for isolation and idempotency
 * **CHANGELOG.md** file is completed by zest-releaser with all commit messages starting 
 after the previous release to the next one
