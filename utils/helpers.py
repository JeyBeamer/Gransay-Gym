def validate_username(username):
    if len(username) < 3 or len(username) > 20:
        return False
    if not username.isalnum():
        return False
    return True

def validate_membership_price(price):
    try:
        price = float(price)
        return price >= 0
    except ValueError:
        return False

def format_currency(amount):
    return "${:,.2f}".format(amount)

def is_valid_plan_details(details):
    return len(details) > 0 and len(details) <= 1000

def sanitize_input(input_string):
    return input_string.strip()