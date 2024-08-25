# Getting Started

I recommend setting up a python virtual environment with this, largely because we are using the
[pybullet library](https://pybullet.org/wordpress/), and [PyFlyt](https://github.com/jjshoots/PyFlyt) environment

## Python venv
### To download and install the venv package
```
sudo apt-get update
sudo apt-get install python3-venv
```

### Activate your venv
```
python<version> -m venv <virtual-environment-name>

Example:
python3.8 -m venv .env
source .env/bin/activate
```

And to deactivate, simply run
```
deactivate
```

## Dependencies
To install all of the required dependencies for this project, simply run (after activating your venv if you're using it)
```
pip install -r requirements
```