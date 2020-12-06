# modeling_network_resilience
## Use Case Diagram
The team identified five main actors that interact with the system: Authorized User, System Administrator, Security Administrator, External Threat Actor, and Internal Threat Actor. 

The entire system is broken down into 4 components: 

* Network Infrastructure:  it is the network that can be internet, WiFi or any other network the user is using to connect to the streaming service 

* Authorization system: This component takes care of the user Authentication and Authorization. 

* Cyber resilience: This is the component that we are integrating into the system that implements cyber-resilience, including Monitoring the data flow throughout the system, sending Intrusion Alerts and generating Reports or a Dashboard.  

* Streaming Service Virtual session: Each user has their own virtual session they start after  successful login into the system. 
The use case scenarios for each actor is defined for the streaming service include:  

The use case diagram covers the following use case scenarios:
Scenario 1: User Access to Data Center - A process by which a general authorized user logs into the Data Center using their credentials.
Scenario 2: System Admin Access to Data Center - A process by which a System Administrator logs into the Data Center using their credentials. 
Scenario 3: Security Admin Access to Data Center - A process by which a Security Administrator logs into the Data Center using their credentials 
Scenario 4: Malicious Actor Penetrates System - A process by which an external malicious actor attacks the system.  
Scenario 5: Insider Threat Actor Penetrates System - A process by which an inside threat actor intentionally attacks or accidentally harms the system.  

## SimPy

Welcome! The purpose of this repository is to provide a demonstration repository of how to model network resilience using python. The focus of this demo is to understanding how changes in tower range and availability affect the ability of users to make calls or connect to towers. 

Key features of each file include: 
* Towers.csv - this file holds basic information about (imaginary) cell towers for demonstration. Update this file with cell tower information of your choosing to test a real world scenario. 
* config.py - this file contains parameters a user can update to define their simulation. You may chose to update this file to experiment with different situations. 
* networks.py - this file contains a basic definition of objects that may be of interest for network modeling likes towers, data centers, and devices. You do not need to update this file to execute the simulation.
* test_networks.py - this file contains a script to test the scenario you define. You will need to run but do not need to change this file to execute the simulation.
* graph_me*.py - these scripts show examples of how you may chose to visualize the results of your simulation. 

## STK
The STK tool was used to simulate the jamming attack. The team used STK to design a network for the communication between a sensor to a controller. To design this the transmitter was implemented in the sensor. A digital transponder was designed in the geo-synchronized satellite with the combination of receiver and a transmitter. The controller has a receiver implemented in it. 
Two jammers were introduced in the simulation. The key idea of jamming is to set the jammer towards the target and the right frequency. 
 * The jammer 1 is not set to the right target and frequency, thus there is no connection to the controller as it has no effect on the network. This part of the model demonstrates the scenario of an unsuccessful jammer. 
 * The jammer 2 is set with the right target and frequency so it can induce noise in the system making a successful attack. Currently the link between the satellite to the controller for the sensor and jammer are not synchronized. With the trial license of STK, the team could not find the right resources in STK to synchronize the communication link in the model. If future programmers can successfully synchronize the communication link, then the jamming attack can be simulated and analyzed

## Arena
