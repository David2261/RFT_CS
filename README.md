<p><a target="_blank" href="https://app.eraser.io/workspace/HiY5EZGTvtp1IQFOxd1Q" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# RFT_CS     
>  Rocket fuel and trajectory computing system
_An application for calculating the amount of rocket fuel and oxidizer used. Numerical simulation of rocket flight, (i.e. simulation of the rocket flight environment). Determination of the coordinates of the flight and landing of the rocket (both for ballistic missiles and for space)_ 

## Are you sure I'm not coming to your house?
The project is based on the use of formulas:

```
- The sum of all velocities affecting the rocket
- The model of the moment of the resistance force
- Rotation matrix
- Gravity losses
- Aerodynamic losses
- Loss of speed on control
- Mass of the rocket structure, etc.
```
## The theoretical part
- Links
_All formulas and calculations can be found in the folder_ [﻿Source](docs/idea/theory/source.md) 
- Calculations
_You can find all computation in the folder:_ [﻿Theory](docs/idea/theory/img/) 
- Documentation
_Project documentation:_ [﻿Docs](docs/) 
## Tools
```
- Python 3.10
- Numpy 1.23
- Scipy 1.9
- Matplotlib 3.5
- flake8 5.0
- pytest 7.1
- poetry 22.1
```
## Develop
1. Install Python 3.9 or later and Poetry 1.3 or later.
2. Clone this repository
3. Run poetry install to install the Python dependencies.
4. Activate environment `source .venv/bin/activate` 
5. Go to `RFTCS/`  directory
6. Run `python3 main.py` 
## Example
```python
def volume_cylindrical_cavity(self):
try:
    log_info.info("Запуск функции 'volume_cylindrical_cavity'")
    R_n = self._cylindrical_cavity()
    V = np.pi * float((R_n**2) * self.L)
except Exception as e:
    logger.error(e)
    sys.exit(1)
return V
```




<!--- Eraser file: https://app.eraser.io/workspace/HiY5EZGTvtp1IQFOxd1Q --->