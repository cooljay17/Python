#Built a User Profile model with name, email, and age — enforced valid email format & age range (18–100) 
from pydantic import BaseModel, EmailStr,  field_validator
from email_validator import validate_email, EmailNotValidError
class UserProfile(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator('name')
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('Name must not be empty')
        return value.strip()
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        try:
            validate_email(value)
        except EmailNotValidError:
            raise ValueError("Invalid email format")
        return value
    
    @field_validator('age')
    def age_must_be_valid(cls, value):
        if value < 18 or value > 100:
            raise ValueError('Age must be between 18 and 100')
        return value
    

user = UserProfile(name="Jay", email="jay@gmail.com", age=25)
print("Correct User:",user)
try:
    user2 = UserProfile(name="", email="hello@hotmail.com", age=20)    
except Exception as e:
    print(f"Validation error: {e}")
try:  
    user3 = UserProfile(name="Alice", email="xyz@gmail.com", age=17)
except Exception as e:
    print(f"Validation error: {e}")
try:  
    user4 = UserProfile(name="Rose", email="he123hotmailcom", age=34)
except Exception as e:  
    print(f"Validation error: {e}")

    

