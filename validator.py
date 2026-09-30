def is_valid_amount(amount):
    """Check whether an expense amount is valid."""

    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


def is_valid_name(name):
    """Check whether an expense name is valid."""

    if not name.strip():
        return False

    return True
