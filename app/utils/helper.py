# app/utils/helper.py
def calculate_tax(price: float, tax_rate: float = 0.1) -> float:
    return price * tax_rate
