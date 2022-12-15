# RFT_CS
> Rocket fuel and trajectory computing system
*An application for calculating the amount of rocket fuel and oxidizer used. Numerical simulation of rocket flight, (i.e. simulation of the rocket flight environment). Determination of the coordinates of the flight and landing of the rocket (both for ballistic missiles and for space)*

[![GitHub stars](https://img.shields.io/github/stars/David2261/RFT_CS)](https://github.com/David2261/RFT_CS/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/David2261/RFT_CS)](https://github.com/David2261/RFT_CS/issues)
[![GitHub license](https://img.shields.io/github/license/David2261/RFT_CS)](https://github.com/David2261/RFT_CS/blob/main/LICENSE)
[![Twitter](https://img.shields.io/twitter/url?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FDavid2261%2FRFT_CS)


## Are you sure I'm not coming to your house?
The project is based on the use of formulas:

	- The sum of all velocities affecting the rocket
	- The model of the moment of the resistance force
	- Rotation matrix
	- Gravity losses
	- Aerodynamic losses
	- Loss of speed on control
	- Mass of the rocket structure, etc.


## The theoretical part
- Links
*All formulas and calculations can be found in the folder* [Source](.idea/theory/source.md)

- Calculations
*You can find all computation in the folder:* [Theory](.idea/theory/img/)

- Documentation 
*Project documentation:* [Docs](.docs/)


## Tools
	- Python 3.10
	- Numpy 1.23
	- Scipy 1.9
	- Matplotlib 3.5
	- flake8 5.0
	- pytest 7.1
	- poetry 22.1


## Install
```bash
poetry install
.venv\Scripts\activate
```

## Example
```python
def addition_lsc(
		time,
		F: float,
		mass: float,
		Alpha: float) -> float:
	Vu = (F / mass) * (1 - np.cos(Alpha))
	return Vu
```
