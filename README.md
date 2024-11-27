# Assignment 1: Two turtles in Turtlesim

This is the main code-base and ROS workstation for the project. The simulation spawns two turtles, and asks you for input. Your input should be a triple, ```turtle_name(turtle1 or turtle2) velocity_x(number) velocity(number)``` and then the specified turtle moves in that direction. It is important to know that the turtles can't bypass the threshold/walls of the environment (1.5<x<9.5 and 1.5<y<9.5), and the turtles can't get close to each other. Distance is published to ```distance``` topic as they move in the environment.
![screenshot](https://github.com/milwd/turtle_ws/blob/master/working%20footage.gif)
## Installation

The project needs Python3, ROS Noetic, and Turtlesim. Make sure to source the setup file.

## Usage

The project incorporates a launch file, so it can be executed altogether with 
```bash 
roslaunch assignment1_rt turt.launch
``` 

The launch file is located inside ```turtle_ws/src/assignment1_rt/launch/```.

## Contributing

Let me know if you cleaned this code :).
