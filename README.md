
# EGM2008 Geoid Model - Peru

Desktop application developed in Python to implement the EGM2008 geoid model for Peru.

The application computes geoid undulation (N) and orthometric height (H) from geodetic coordinates using bilinear interpolation over the official EGM2008 Peru grid.

## Features

- Load the EGM2008 Peru grid from an Excel dataset.
- Compute grid indices (i, j).
- Retrieve surrounding grid vertices.
- Perform bilinear interpolation.
- Compute geoid undulation (N).
- Compute orthometric height (H = h − N).
- Desktop graphical user interface.

## Technologies

- Python 3
- Pandas
- OpenPyXL
- PySide6
- Git

## Project Structure

```
data/
icon/
main.py
egm2008.py
interpolation.py
calculations.py
ui.py
utils.py
```

## Status

Work in progress... XD

## Author

Marcelo Benites
Software Engineering Student
=======
# ModeloGeoidalEGM2008
Desktop application for geoid height interpolation using the EGM2008 model for Peru.
>>>>>>> a455a60 (Initial commit)
