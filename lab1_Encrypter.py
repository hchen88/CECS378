
"""
CECS 378
Lab 1 Encrypter
June 4, 2019
@author: Howard Chen
Professor Giacalone
Purpose: This program encrypts using simple-substitution

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
    for letter in keyString: #converts keyString to keyList
        keyList.append(letter)
        
    print("Key: ") #outputs keylist
    print(keyList)
    
    for char in msg: #iterates through message one char at a time
        char = char.lower() #makes any uppercase letter lower
        if(char.isalpha()):
            encryptedString += keyList[ord(char) - 97]#encrypts letter with key
        else:
            encryptedString += char #appends any noncharacters without encrypt
    print("Encrpyted Msg: " + encryptedString)
    
#prompt user to enter phrase to encrypt    
msg = input("Please enter in a phrase to encrypt: ")

#loops until user enters valid 26 char key
while(len(keyString) != 26 ): 
    keyString = input("Please enter in a key (26 char): ") #prompts user for key
    if(len(keyString) != 26): #checks for 26 char length for key
        print("Invalid Key is not 26 char in length! Retry") #prints error msg

#calls function to encrypt 
encrypt(msg, keyString)







    
