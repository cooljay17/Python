#Generate a random 8-character password
import random
import string

length = 8
password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print("Password Created:",password)