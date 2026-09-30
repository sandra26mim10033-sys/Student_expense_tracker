def get_category(name):
    """Return a category based on the expense name."""

    name = name.lower()

    if "food" in name or "lunch" in name or "dinner" in name:
        return "Food"

    if "bus" in name or "train" in name or "travel" in name:
        return "Travel"

    if "book" in name or "study" in name:
        return "Education"

    return "Other"