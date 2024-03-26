---
title: RoboRIO
description: 
published: true
date: 2024-03-26T04:51:57.468Z
tags: 
editor: markdown
dateCreated: 2024-03-26T04:39:28.504Z
---

# RoboRIO
The RoboRIO is the brains of the robot. This is where all of the code is ran, and where things like the can bus and the RSL plug into.

![rio.png](/rio.png){.align-center}


There are many ports on the Rio, some of the most important of which are:

<details>
  <summary>Input Power</summary>
  This is how you power the Rio. It needs (insert V and A) power, and should be powered either off of the VRM or one of the low power slots on the PDH. To insert wires into this terminal, you have to get a very small flathead screwdriver and unscrew the screws on the side of the terminal until you can insert the wires through the top. Then, screw these screws back in until they are tight and the wires don't come out when pulled.
</details>

<details>
  <summary>USB Device</summary>
  This is a USB-B port, and can be used to connect to the Rio. This can be used as an alternative to ethernet when trying to connect
</details>

<details>
  <summary>USB Host</summary>
  These are both USB-A ports, and are used to plug in peripherals to the Rio. These are most commonly things like USB cameras, and flash drives for collecting logs.
</details>

<details>
  <summary>Ethernet</summary>
  This ethernet port is what you usually use to communicate with the Rio. this is usually plugged in to the ethernet switch, but can also be plugged in directly to the radio if there are no other ethernet devices on the robot.
</details>

<details>
  <summary>LEDs</summary>
  These LEDs can be used to see the status of the Rio, which can be found [here](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html)
</details>

<details>
	<summary>Reset and User Buttons</summary>
  These buttons are mostly used for resetting the Rio. This is most useful for when the Rio is E-Stopped, and instructions for undoing this can be found [here](TODO: link)
</details>

<details>
	<summary>Robot Signal Light</summary>
  This is the port for the [RSL](/index.html?path=Components/RSL.md). When plugging this in, make sure to plug in the black wire to the port closest to the edge.
</details>

<details>
	<summary>DIO</summary>
  These are DIO (Digital Input Output) ports. These ports can be used to read data from external sensors. This includes things like linebreak sensors, limit switches and more.
</details>

<details>
	<summary>CAN</summary>
  This is where the CAN bus starts. To insert the CAN wires, press down on the white button, and then insert the wire. Make sure the wire is secure by pulling on it. 
</details>