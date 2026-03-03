import re
import json
from decimal import Decimal


def normalize_price(price_str):
    """
    Convert price like '1 200,00' → Decimal('1200.00')
    """
    cleaned = price_str.replace(" ", "").replace(",", ".")
    return Decimal(cleaned)


def extract_prices(text):
    """
    Extract all monetary values that look like prices.
    Matches:
    308,00
    1 200,00
    7 330,00
    """
    price_pattern = r'\d{1,3}(?:\s\d{3})*,\d{2}'
    return re.findall(price_pattern, text)


def extract_products(text):
    """
    Extract product names.
    Matches numbered product entries:
    1.
    Product Name
    """
    product_pattern = r'\d+\.\s*\n(.+?)\n'
    return re.findall(product_pattern, text)


def extract_datetime(text):
    """
    Extract date and time.
    Example:
    Время: 18.04.2019 11:13:58
    """
    dt_pattern = r'Время:\s*([\d\.]+\s[\d:]+)'
    match = re.search(dt_pattern, text)
    return match.group(1) if match else None


def extract_payment_method(text):
    """
    Extract payment method.
    Example:
    Банковская карта:
    """
    payment_pattern = r'(Банковская карта|Наличные|Карта):'
    match = re.search(payment_pattern, text)
    return match.group(1) if match else None


def extract_total(text):
    """
    Extract total amount after 'ИТОГО:'
    """
    total_pattern = r'ИТОГО:\s*\n?([\d\s,]+)'
    match = re.search(total_pattern, text)
    if match:
        return normalize_price(match.group(1))
    return None


def calculate_items_total(prices, text):
    """
    Calculate total based only on item final prices
    (ignore duplicate 'Стоимость' lines if needed)
    """
    # Extract only prices that appear after quantity lines (final item price)
    item_price_pattern = r'\d+,\d{3}\s*x\s*[\d\s,]+\n([\d\s,]+)'
    item_prices = re.findall(item_price_pattern, text)

    total = Decimal("0.00")
    for price in item_prices:
        total += normalize_price(price)

    return total


def main():
    with open("raw.txt", "r", encoding="utf-8") as f:
        text = f.read()

    prices = extract_prices(text)
    products = extract_products(text)
    datetime_info = extract_datetime(text)
    payment_method = extract_payment_method(text)
    total_amount = extract_total(text)

    structured_output = {
        "products": products,
        "prices_found": prices,
        "total_amount": str(total_amount) if total_amount else None,
        "date_time": datetime_info,
        "payment_method": payment_method
    }

    print(json.dumps(structured_output, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
