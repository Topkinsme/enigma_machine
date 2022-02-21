# enigma_machine
A python package that allows a user to encrypt a message, simulating an enigma machine.

Examples
```py
import enig
from enig import em
mac=em.Enigma_Machine()
print(mac.rotor1,mac.rotor2,mac.rotor3)
>>> 1 1 1
mac.random_rotors()
print(mac.rotor1,mac.rotor2,mac.rotor3)
>>> 14 12 20
res=mac.result("Hello, World!")
>>> shbkh, tgoye!
```
