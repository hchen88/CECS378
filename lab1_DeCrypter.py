
"""
CECS 378
Lab 1 Decrypter
June 4, 2019
@author: Howard Chen
Professor Giacalone
Purpose: This program decrypts using simple-substitution

"""

#key in the form of a string
keyString = ""


"""
decrypt function definition 
parameters : msg- msg to be decrypted as a string
            keyString - key as a string 
return : none
"""
def decrypt(msg, keyString):
    keyList = [] #key in list variable
    decryptedString = "" #decrpyted empty string
    #list of alphbets makes it easier to convert letters
    alphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
                    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                    "x", "y", "z"] 
    for letter in keyString: #loops through keystring one letter at a time
        keyList.append(letter) #appends to empty keylist
        
    print("Key: ") #prints keylist
    print(keyList)
    
    for char in msg: #iterates through msg to decrypt one letter at a time
        char = char.lower() #makes any uppercase letter lower
        if(char.isalpha()): #checks if chartacter is a letter.
            #converts to correct letter
            decryptedString += alphaList[keyList.index(char)] 
        else: 
            decryptedString += char #concantenates any spaces or punctuations 
    print("Decrpyted Msg: " + decryptedString)
    
#prompt user to enter phrase to encrypt    
msg = input("Please enter in a phrase to decrypt: ")
#loops until keyString is a valid 26 characters
while(len(keyString) != 26 ):
    #prompts for key
    keyString = input("Please enter in a key (26 char): ")
    #checks for length
    if(len(keyString) != 26):
        print("Invalid Key is not 26 char in length! Retry")
#decrypt function call
decrypt(msg, keyString)







    
