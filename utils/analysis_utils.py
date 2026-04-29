"""Utils for analyzing account information."""

red_flag = "\U0001F534"
yellow_flag = "\U0001F7E1"
green_flag = "\U0001F7E2"

def process_account_age(account_age):
    """Evaluate account age."""
    if account_age.days > 3*365:
        return green_flag
    elif account_age.days > 90:
        return yellow_flag
    else: 
        return red_flag