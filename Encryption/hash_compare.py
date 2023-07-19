import hashlib


def SHA1(text):
    myHash = hashlib.sha1()
    text = bytes(text, 'utf-8')
    myHash.update(text)
    return myHash.hexdigest()

def SHA224(text):
    myHash = hashlib.sha224()
    text = bytes(text, 'utf-8')
    myHash.update(text)
    return myHash.hexdigest()

def SHA256(text):
    
    myHash = hashlib.sha256()
    text = bytes(text, 'utf-8')
    myHash.update(text)
    print(myHash.hexdigest())
    return myHash.hexdigest()

def SHA384(text):
    myHash = hashlib.sha384()
    text = bytes(text, 'utf-8')
    myHash.update(text)
    return myHash.hexdigest()

def SHA512(text):
    myHash = hashlib.sha512()
    text = bytes(text, 'utf-8')
    myHash.update(text)
    return myHash.hexdigest()


def MD5(text):
    myHash = hashlib.md5()
    hash = bytes(text, 'utf-8')
    myHash.update(hash)
    print(myHash.hexdigest())
    
   
    return myHash.hexdigest()

def validIntegrity(text, hash):
    print("Which algorithm would you like to compare hashes with?")
    algChoice = str(input("1.)SHA1 \n2.)SHA224 \n3.)SHA256 \n4.)SHA384 \n5.)SHA512 \n6.)MD5\n:"))
    algDict = {'1':'SHA1', '2':'SHA224', '3':'SHA256', '4':'SHA384', '5':'SHA512', '6':'MD5'}

    print(algChoice, algDict.keys())
    if algChoice in algDict.keys():
        if(algChoice == '1'):
            return hash == SHA1(text)
        elif(algChoice == '2'):
            return hash == SHA224(text)
        elif(algChoice == '3'):
            return hash == SHA256(text)
        elif(algChoice == '4'):
            return hash == SHA384(text)
        elif(algChoice == '5'):
            return hash == SHA512(text)
        elif(algChoice == '6'):
            print(hash, MD5(text))
            return hash == MD5(text)
        else:
            return "Something went wrong"
    else:
        return "Invalid message plese try again."
    
with open('password_hashes.txt','r+') as f:
    if(f.readable()):
        passHash = f.readline().replace(" - ", ",").replace("[","").replace("]","").split(",")
        text, hash= passHash[0].split(":").pop(1), passHash[1].split(":").pop(1)
        print(text)
        print(passHash)
        valid = validIntegrity(text, hash)
        print(valid)
    else:
        print("Not reading")
    # print(valid)
