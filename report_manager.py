from collections import defaultdict
from category_manager import get_category

def category_totals(expenses):
    """Calculate total spending for each category."""

    totals = defaultdict(float)

    for expense in expenses:
        category = expense.get("category") or get_category(expense["name"])
        totals[category] += expense["amount"]

    return dict(totals)