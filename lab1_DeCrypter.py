# -*- coding: utf-8 -*-
"""
@author Howard Chen

"""

#encrypted string

#key in the form of a list
keyList = []
keyString = ""


"""
encrypt function definition 
parameters : msg- msg to be encrypted as a string
            keyString - key as a string 
return : none
"""
def decrypt(msg, keyString):
    decryptedString = ""
    alphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
                    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                    "x", "y", "z"]
    for letter in keyString:
        keyList.append(letter)
        
    print("Key: ")
    print(keyList)
    
    for letter in msg:
        letter = letter.lower() #makes any uppercase letter lower
        if(letter.isalpha()):
            decryptedString += alphaList[keyList.index(letter)]
        else:
            decryptedString += letter
    print("Decrpyted Msg: " + decryptedString)
    
#prompt user to enter phrase to encrypt    
msg = input("Please enter in a phrase to decrypt: ")

while(len(keyString) != 26 ):
    keyString = input("Please enter in a key (26 char): ")
    if(len(keyString) != 26):
        print("Invalid Key is not 26 char in length! Retry")

decrypt(msg, keyString)







    
