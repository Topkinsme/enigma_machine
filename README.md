# enigma_machine
A python package that allows a user to encrypt a message, simulating an enigma machine.

Examples
```py
from enig import Enigma_Machine 
mac=Enigma_Machine()
print(mac.rotor1,mac.rotor2,mac.rotor3)
>>> 1 1 1
mac.random_rotors()
print(mac.rotor1,mac.rotor2,mac.rotor3)
>>> 14 12 20
res=mac.result("Hello, World!")
>>> shbkh, tgoye!
```
