from MainModuleADM.Encryption.aes import i_decrypt, i_encrypt


test = 'Initial Project Testing'
key = 'WKbWo%Grj)C6YhAq'[:16]

testEncrypt = i_encrypt(key,test)
print(testEncrypt)

testDecrypt = i_decrypt(key, 'jbXu0q7Xm/LgoGL2qR3R324vz94QjecDoGGvh1T9P2dxIARXuN0pQ1bj7jo16A0/')

print(testDecrypt)