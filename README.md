# Ideal Gas Simulation Project

This Python project utilizes the Pygame library to simulate the behavior of an ideal gas with static collisions between particles, following the Maxwell distribution. The ideal gas model is a theoretical model that describes the behavior of a gas under certain ideal conditions.


<p align="center">
<img alt="Animation of an ideal gas simulation in a 2D container. Multiple colored atoms are randomly moving and colliding with each other. The collisions are elastic, with atoms bouncing off each other and the walls of the container. The movement of the atoms creates a dynamic and chaotic pattern within the container.", src="https://github.com/daviromao/gas-project/assets/53953664/7dfb8b39-de3d-4708-827d-ae1978048841" width="30%"/>
</p>



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
