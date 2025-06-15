#Validate gmail using regex
import re
def validate_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    if re.match(pattern, email):
        return True
    else:
        return False
    
email=input("Enter a valid gmail id: ")
retVAl=validate_gmail(email)
if retVAl:
    print("It is a valid gmail id")
else:
    print("It is an invalid gmail id")    