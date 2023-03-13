class InvalidPasswordFormatError(ValueError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Reason: {}".format(self.message)

def is_valid_password(pswd):
    if len(pswd) < 8 and not pswd.isalpha():
        raise InvalidPasswordFormatError("Your password is too short. Your password must contain only letters.")
    elif len(pswd) < 8:
        raise InvalidPasswordFormatError("Your password is too short.")
    elif not pswd.isalpha():
        raise InvalidPasswordFormatError("Your password must contain only letters.")
    else:
        return True

if __name__ == "__main__":
    try:
        print(is_valid_password("abcde8"))
    except InvalidPasswordFormatError as e:
        print(e)
