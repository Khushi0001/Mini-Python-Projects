import random
import string as str
s1=str.ascii_lowercase
s2=str.ascii_uppercase
s3=str.digits
s4=str.punctuation
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
l=int(input("\nEnter the length of password \n "))
print("\nYour Password: ")
print("".join(random.sample(s,l)))


# import random
# s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
# l=int(input("\nEnter the length of your Password\n"))
# print("Your Password:\n")
# print("".join(random.sample(s,l)))
