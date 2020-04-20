#email slicer validators 
#Instale "email_validator" via pip

from email_validator import validate_email, EmailNotValidError

email = "marceloandre.garcia@gmail.com"

try:
    v = validate_email(email) 
    email = v["email"] 
    print("VALID EMAIL")
    
except EmailNotValidError as e:

    print(str(e))