# Usage and Research Guidelines
---------------------------------

This little build system for data science projects was directly forked from https://github.com/drivendata/cookiecutter-data-science. The principles are based on their [blog article](http://drivendata.github.io/cookiecutter-data-science/) for reproducible collaborative data science projects. We've made some tweaks to the project
structure and developed a build system that suits our needs, but the basic principles from this article should be followed. 




## How to Use this Repo and Best Practices
-----------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile controller with development commands
├── README.md          <- The top-level README for developers using this project.
│
├── requirements.txt    <- The requirements file for reproducing the project environment. This is 
│                         seperate from the ``setup.py`` which contains requirements for the 
│                         build system and should not be modified.
│
├── {{cookiecutter.package_name}}       <- User defined code for this project. 
│   ├── __init__.py                     <- Contains public imports from _build_system package that can be used
│   ├── _version.py                     <- package version data (bump this and git tag to create dev cycles)
│   ├── dal.py                          <- data acess layer to control database operations
│   ├── model.py                        <- placeholder for models
│           ...                         <- Any developed python code for maintaining reproducibilty using APIs in build system
│
│
└── HISTORY.md            <- for tracking changes to the project package
```

This is very similar to the original cookie-cutter but we've added some features to improve the build system which will be outlined below in detail.



### Installation and Overview

To install a fresh project add new packages to requirements.txt, initialize a new git repository, create a virtual environment with your method of choice and run. Note that if you are adding from github you should add it as ``<package_name> @ git+<github_link>`` since we are using setuptools.

```{bash}
$ make install
```

This will install your requirements.txt. 

### Docker
If you don't have docker engine and compose, find out about installing here: https://docs.docker.com/engine/install/ and https://docs.docker.com/compose/install/ respectivley.





