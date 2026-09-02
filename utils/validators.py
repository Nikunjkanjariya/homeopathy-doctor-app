import re

def validate_phone(phone):
    """Validate phone number"""
    pattern = r'^[0-9]{10,15}$'
    phone_clean = re.sub(r'[\s\-\(\)]', '', phone)
    return re.match(pattern, phone_clean) is not None

def validate_email(email):
    """Validate email address"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_pincode(pincode):
    """Validate pincode/zip code"""
    pattern = r'^[0-9]{5,10}$'
    return re.match(pattern, pincode) is not None

def validate_date(date_string, format='%Y-%m-%d'):
    """Validate date format"""
    try:
        from datetime import datetime
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False
