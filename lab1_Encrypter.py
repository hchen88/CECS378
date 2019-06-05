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
def encrypt(msg, keyString):
    encryptedString = ""
    for letter in keyString:
        keyList.append(letter)
        
    print("Key: ")
    print(keyList)
    
    for letter in msg:
        letter = letter.lower() #makes any uppercase letter lower
        if(letter.isalpha()):
            encryptedString += keyList[ord(letter) - 97] 
        else:
            encryptedString += letter
    print("Encrpyted Msg: " + encryptedString)
    
#prompt user to enter phrase to encrypt    
msg = input("Please enter in a phrase to encrypt: ")

while(len(keyString) != 26 ):
    keyString = input("Please enter in a key (26 char): ")
    if(len(keyString) != 26):
        print("Invalid Key is not 26 char in length! Retry")

#calls function to encrypt 
encrypt(msg, keyString)







    
