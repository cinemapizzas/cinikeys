import random
import time

print("\n##################################")
for i in range(1):
 print("#                                #")
time.sleep(0.3)
print("#      welcome to  ciniKeys      #")
time.sleep(0.3)
for i in range(1):
  print("#                                #")
time.sleep(0.3)
print("##################################")

for i in range(1,2):
    print("\n"*i)
    time.sleep(0.3)

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&1234567890'


numberOfPasswords = int(input('Amount of passwords you wish to generate: '))

length = int(input('Please input your desired password length: '))

print(" results +++++++ ")
for i in range(0,3,1):
    print("               +")
    time.sleep(0.3)

print("               V")
print("               ")


for i in range (1,numberOfPasswords):
    password =''
    for c in range(length):
        password += random.choice(chars)
    print("password" + str(i) + ": ", password)
    time.sleep(0.3)

print("\n###################################")
for i in range(1):
 print("#                                 #")
time.sleep(0.3)
print("#  ♥ Thanks for using cinikeys ♥  #")
for i in range(1):
 print("#                                 #")
time.sleep(0.3)
print("###################################")