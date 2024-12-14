class PaymentError(Exception):
    """Custom exception class to indicate a payment processing error."""
    pass


class InventoryError(Exception):
    """Custom exception class to indicate an inventory problem."""
    pass  # 'pass' is again used because no extra functionality is needed here.


def process_payment(payment_amount):
    """
    Simulates a function that processes payments.
    'payment_amount': This is the input parameter representing the payment amount to process.
    It must be a positive number. If it is negative, a PaymentError will be raised.
        """
    if payment_amount < 0:
        raise PaymentError("Payment amount cannot be negative")


def update_inventory(item_id):
    """
    Simulates a function that updates inventory.
    'item_id': This is the input parameter representing the ID of the item to be checked in the inventory.
    The function raises an InventoryError if the item is out of stock.
    """
    if item_id == "out_of_stock":
        raise InventoryError("Item is out of stock")


def place_order(payment_amount, item_id):
    """
    Simulates placing an order by processing payment and updating inventory.
    'payment_amount': The amount to be paid for the order.
    'item_id': The ID of the item to be checked in the inventory.
    """
    try:
        process_payment(payment_amount)
        update_inventory(item_id)
    except PaymentError as pe:
        raise RuntimeError(
            "Order could not be placed due to payment failure") from pe
    except InventoryError as ie:
        raise RuntimeError(
            "Order could not be placed due to inventory issue") from ie


try:
    place_order(-50, "item_123")
except RuntimeError as re:
    print(f"Error: {re}")
try:
    place_order(100, "out_of_stock")
except RuntimeError as re:
    print(f"Error: {re}")
