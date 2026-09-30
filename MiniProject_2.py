# import random
# import string

# print(string.ascii_letters)    #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase)  #abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase)  #ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)           #0123456789
# print(string.punctuation)      #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# charValues = string.digits + string.ascii_letters + string.punctuation
# print(charValues)              #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# print(random.choice(charValues))

# list_comprehension = [function for i in range (n)]
# pass_len = 12
# password = "".join([random.choice(charValues) for i in range(pass_len)])
# print(password)             #a random password will be generated


# RANDOM PASSWORD GENERATOR

import random
import string

pass_len = 12
charValues = string.digits + string.ascii_letters + string.punctuation

password = "".join([random.choice(charValues) for i in range(pass_len)])

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

print(password)