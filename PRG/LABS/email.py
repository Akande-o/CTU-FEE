"""
Single e-mail handling
"""


class IncorrectEmailError(ValueError):
    """E-mail in incorrect format"""


class Email:
    """A single e-mail address"""

    def __init__(self, address):
        if "@" not in address:
            raise IncorrectEmailError("Incorrect e-mail format")

        self.address = address

    def __str__(self):
        local, domain = self.address.split("@")
        anonymized_local = local[:3] + "*" * (len(local) - 3)
        return f"{anonymized_local}@{domain}"

    @property
    def top_level_domain(self):
        """Return the last dot-separated part of the domain (after @)"""
        _, domain = self.address.split("@")
        top_level = domain.split(".")[-1]
        return top_level

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.address == other.address
        elif isinstance(other, str):
            return self.address == other
        return False

    @staticmethod
    def suggest_different_email(email):
        """Given an email address, suggest a different one e.g. when the e-mail is taken"""
        local, domain = email.address.split("@")
        return f"{local}2@{domain}"


class Gmail(Email):
    """A single e-mail address on gmail domain"""

    domain = "gmail.com"

    def __init__(self, username):
        super().__init__(f"{username}@{self.domain}")


#
# Extra functions, outside the assignment
#

def load_email(path):
    """Load email from given path. Return a new Email instance given data under the path"""
    with open(path, "r") as handle:
        address = handle.read()
    
    return Email(address)
