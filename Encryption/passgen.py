from random import randint
import hashlib
import os

myHash = hashlib.md5()
specialChar = ["#" , "@", "?", "[", "]", "{", "}", "/", "_", "-", "^", "`", "|" ]
password = []
for i in range(0,6):
    lowerChar = (randint(97,122))
    print(chr(lowerChar), lowerChar)
    password.append(chr(lowerChar))

    upperChar = (randint(65,90))
    print(chr(upperChar), upperChar)
    password.append(chr(upperChar))

    randChar = randint(0, len(specialChar) -1)
    password.append(specialChar[randChar])

    password.append(str(randint(0,9)))
    
   


password, passwordBytes = "".join(password), bytes("".join(password), 'utf-8')
myHash.update(passwordBytes)

hash = myHash.hexdigest()


with open('password_hashes.txt', 'w') as f:
    f.write(f"[PASSWORD:{password}] - [HASH:{hash}]")

