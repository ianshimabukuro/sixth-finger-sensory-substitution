# Sixth Finger Sensory Substitution Device
Made at Biomechanics Lab, University of Tsukuba

*by Ian Shimabukuro*

## Description
Code for the control of a sixth finger activated by a pressure sensor. Plays different sounds based on activation pressure using Garageband


## Pressure to Sound

The pressure values are mapped to an array, each array item represents a keyboard key. Based on the pressure value, we press a key in a Macbook Air keyboard while having garageband open.

This plays different piano keys depending on the pressure values *(pressure : [0,1023], keys : [C,D,E,F,G,A,B])*

## Pressure to servo angle

The pressure values are mapped to angular values and then used to activate a servo motor.


