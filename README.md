[![Build Status](http://ec2-52-212-162-0.eu-west-1.compute.amazonaws.com:8080/buildStatus/icon?job=bdacore%2Fmaster)](http://ec2-52-212-162-0.eu-west-1.compute.amazonaws.com:8080/job/bdacore/job/master/)


What is this?
===============

BDA core library of data science and data manipulation functions.

# How do I install it

First, make sure you have miniconda or anaconda installed. If not, `install it! <https://conda.io/docs/user-guide/install/index.html>`_


Then you can install bdacore by running::

    make install

This will install the main requirements for running the bdacore lib. If you use advanced methods, you may need to
install extra packages.

If you want to install all required packages at once, then run::

    make develop_env

You may want to override the default package name (bdacore) and Python version (3.6). This can be done by overriding the *ENV_NAME* and *ENV_PY_VERSION* as follows::

    make develop_env ENV_NAME=bdacore_py2 ENV_PY_VERSION=2.7
# Where can I see some examples?

Check the [documentation of DataDriver's project](http://datadriver-doc-ddapi.s3-website-eu-west-1.amazonaws.com/bdacore/)

A good entry point is to check the [tutorials](http://datadriver-doc-ddapi.s3-website-eu-west-1.amazonaws.com/bdacore/tutorial.html).


# Contributors

This repository is a part of the DataDriver project.
 
Since 2016, there were many people who contributed to this project : 

* Ali El Moussawi
* Arthur Baudry
* Augustin Grimprel
* Aurélien Massiot
* Benjamin Joyen-Conseil
* Constant Bridon
* Cyril Vinot
* Eric Biernat
* Jeffrey Lucas
* Nicolas Cavallo
* Nicolas Frot
* Matthieu Lagacherie  
* Mehdi Houacine
* Pierre Baonla Bassom
* Rémy Frenoy
* Romain Ayres
* Samuel Rochette
* Thomas Vial
* Veltin Dupont 
* Vincent Levorato
* Yannick Drant
* Yannick Schini
* Yasir Khan



## Test datasets

Datasets for testing are made available under the 
Public Domain Dedication and License v1.0 whose 
full text can be found at: http://www.opendatacommons.org/licenses/pddl/1.0/