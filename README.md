# Ideal Gas Simulation Project

This Python project utilizes the Pygame library to simulate the behavior of an ideal gas with static collisions between particles, following the Maxwell distribution. The ideal gas model is a theoretical model that describes the behavior of a gas under certain ideal conditions.




## Simulation

- The particles are represented as circles in the simulation environment.
- Collisions between particles and the container walls are treated as elastic collisions.
- The direction and velocity of particles are updated in each frame of the simulation.

## Maxwell Distribution
- The velocity distribution of particles follows the Maxwell-Boltzmann distribution, which describes the statistical distribution of molecular velocities in an ideal gas at thermal equilibrium.
- The gas temperature, in Kelvin, is a parameter that affects the velocity distribution.

## Atomic Mass

- The particles can have different atomic masses, allowing for the simulation of different types of elements.
- The atomic mass influences the behavior of particles, such as their velocity and kinetic energy.

# How to run the project

### Clone this repository:
```
git clone git@github.com:daviromao/gas-project.git
```

### Create a virtual environment:
```
python -m venv venv
```

### Activate the virtual environment:

- on Windows:
```
.\env\Scripts\activate               
```

- on Ubuntu:
```
source env/bin/activate
```

### Install the dependencies:
```
pip install -r requirements.txt
```

### Run the project:
```
python main.py
```

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.