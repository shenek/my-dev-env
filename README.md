# My Dev Env

This is a meta package which can be installed to download and install other dependencies
used for development in python. It is a kind of collection of development packages used
for various configurations.


## Installation

It is prefered to install this package into your virtual environment after the initialization of the environment. So you can used the development tools right from the start.

To install it, you can simply run:

```bash
pip install my-dev-env
```


This will install just a basic set of packages. You can also install wider range of packages:

```bash
pip install my-dev-env[django]
```


Currently you can install packages from these extra collections:

* `node`
* `django`
* `release`
