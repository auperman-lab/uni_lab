p = 47
q = 59
decrypt = 157
n = p * q
phi = (p - 1) * (q - 1)
encrypt = 0

for i in range(1, phi):
    if ((decrypt % phi) * (i % phi)) % phi == 1:
        encrypt = i

message = int(input())

encryptmessage = message**encrypt % n
print('Encrypted message is : ', encryptmessage)

decryptmessage = encryptmessage**decrypt % n
print('Dencrypted message is : ', decryptmessage)
