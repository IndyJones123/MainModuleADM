import re

def is_valid_email(email: str) -> bool:
    return re.match(r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b$', email) is not None

def is_valid_phone(phone: str) -> bool:
    return re.match(r'^\+62\d{9,15}$', phone) is not None

def is_strong_password(password: str) -> bool:
    return len(password) >= 8 and \
           any(c.isupper() for c in password) and \
           any(c.islower() for c in password) and \
           any(c.isdigit() for c in password) and \
           any(c in '!@#$%^&*()-_+=' for c in password)

def is_valid_ktp(ktp: str) -> bool:
    return ktp.isdigit() and len(ktp) == 16


