# enigma_machine
A python package that allows a user to encrypt a message, simulating an enigma machine.

Examples-
**Simplest form**
```py
import enig
from enig import em
mac=em.Enigma_Machine()
print(mac.result("Hello, World!"))
>>> rsnyf, gidsm!
```
**Different ways to set the rotors**
```py
import enig
from enig import em
mac=em.Enigma_Machine()
#default rotor values are 1,1,1
print(mac.rotor1,mac.rotor2,mac.rotor3)
>>> 1 1 1
mac.result("Hello, World!")
>>> rsnyf, gidsm!
#random rotors
mac.random_rotors()
>>> Your rotor number is 20 22 15
print(mac.rotors()) #Using a methord to view rotors instead of the variables directly
>>> (20, 22, 15)
mac.result("Hello, World!")
>>> wgqgt, sivcz!
#set values
mac.set_rotors_as(23,4,1)
print(mac.rotors())
>>> (23, 4, 1)
mac.result("Hello, World!")
>>> dzkzp, eywix!
```
**Different ways to set up a plugboard**
```py
#Output without plugboard
mac.set_rotors_as(23,4,1)
print(mac.rotors())
>>> (23, 4, 1)
mac.result("Hello, World!")
>>> dzkzp, eywix!
#Setting up a plug board the long way
mac.plug_board_init({'1f': 'a', '1s': 'b', '2f': 'c', '2s': 'd', '3f': 'e', '3s': 'f', '4f': 'g', '4s': 'h', '5f': 'i', '5s': 'j', '6f': 'k', '6s': 'l', '7f': 'm', '7s': 'n', '8f': 'o', '8s': 'p', '9f': 'q', '9s': 'r', '10f': 's', '10s': 't'})
print(mac.plug_list)
>>> {'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h', 'i': 'j', 'k': 'l', 'm': 'n', 'o': 'p', 'q': 'r', 's': 't'}
#Setting up the same plug board the short way
print(mac.quick_plug_board("abcdefghijklmnopqrst")) #this method also returns the dict
>>> {'1f': 'a', '1s': 'b', '2f': 'c', '2s': 'd', '3f': 'e', '3s': 'f', '4f': 'g', '4s': 'h', '5f': 'i', '5s': 'j', '6f': 'k', '6s': 'l', '7f': 'm', '7s': 'n', '8f': 'o', '8s': 'p', '9f': 'q', '9s': 'r', '10f': 's', '10s': 't'}
print(mac.plug_list)
>>> {'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h', 'i': 'j', 'k': 'l', 'm': 'n', 'o': 'p', 'q': 'r', 's': 't'}
#output with plugboard
mac.set_rotors_as(23,4,1)
mac.result("Hello, World!")
>>> dnlzp, fnwjx!
```
