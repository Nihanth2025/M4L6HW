import random
import string

print("Welcome to password generator!")
length=int(input("Enter the length of password:"))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
number=string.digits
Symbol=string.punctuation
a=lower+upper+number+Symbol
temp=random.sample(a,length)
password="".join(temp)
print(password)