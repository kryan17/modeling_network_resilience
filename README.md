# modeling_network_resilience

Welcome! The purpose of this repository is to provide a demonstration repository of how to model network resilience using python. The focus of this demo is to understanding how changes in tower range and availability affect the ability of users to make calls or connect to towers. 

Key features of each file include: 
* Towers.csv - this file holds basic information about (imaginary) cell towers for demonstration. Update this file with cell tower information of your choosing to test a real world scenario. 
* config.py - this file contains parameters a user can update to define their simulation. You may chose to update this file to experiment with different situations. 
* networks.py - this file contains a basic definition of objects that may be of interest for network modeling likes towers, data centers, and devices. You do not need to update this file to execute the simulation.
* test_networks.py - this file contains a script to test the scenario you define. You will need to run but do not need to change this file to execute the simulation.
* graph_me*.py - these scripts show examples of how you may chose to visualize the results of your simulation. 
