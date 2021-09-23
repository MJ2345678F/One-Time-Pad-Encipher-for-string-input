alpha ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext=input('Enter plain text:').replace("  ","  ")
key=input('Enterkey:').replace("","")
print('\n')
#Encryption
cipherText=''
for i in range(len(plaintext)):
    if plaintext[i] in alpha and key[i] in alpha:
        textIndex=alpha.index(plaintext[i])
        keyIndex=alpha.index(key[i])
        sumindex=textIndex+keyIndex
        if sumindex>25:
            sumindex-=25
        cipherText+=alpha[sumindex]
print('Encrypted Text=',cipherText)
decryptedText=' '
#decryption
for i in range(len(cipherText)):
    if cipherText[i] in alpha and key[i] in alpha:
        textIndex = alpha.index(cipherText[i])
        keyIndex = alpha.index(key[i])
        subtractindex = textIndex - keyIndex
        if subtractindex<0:
             subtractindex+=25
        decryptedText+=alpha[subtractindex]

print('decrypted text=',decryptedText)