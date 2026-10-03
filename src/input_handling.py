from email_validator import validate_email, EmailNotValidError
def user_info():
    name = input("name : ")
    while True:
        email = input("email : ")
        try:
            email_info = validate_email(email, check_deliverability=True)
            email = email_info.normalized
            return(name, email)
        
        except EmailNotValidError as e:
            print(f"ایمیل نامعتبر است: {str(e)}")