# OpenCV Face & Motion Tracker

## Installation & Setup

Setup Python
[virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/), then use the following commands to activate the virtual environment and install prerequisites.

```
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

*The following instructions will be automated in the future.*

Create the following folders if they do not exist.

```
mkdir ScreenShots
mkdir Videos
```

Depending on your webcam, you might have to change the two variables under Extensions.py to change the output scale. If the output scale is too large, it can cause issues with tracking and/or lead to performance issues.


## How to use?
Start the program by running Main.py using the following command

```
python3 Main.py
```

### Controls

These controls can be customized under KeyMapping.py

```
q = exits program
r = toggles recording
s = takes a screenshot of the current frame 
```

## Demo

> TBA