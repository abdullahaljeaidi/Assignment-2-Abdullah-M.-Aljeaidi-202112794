from datetime import date

from ebook import EBook, Customer, PrintedEBook, ShoppingCart, Order, Invoice, Payment

def test_add_modify_remove_ebook():
    print("Testing Add/Modify/Remove E-Book")

    # Adding e-books to the catalog
    ebook1 = EBook("1984", "George Orwell", date(1949, 6, 8), "Dystopian", 8.99)
    ebook2 = EBook("To Kill a Mockingbird", "Harper Lee", date(1960, 7, 11), "Fiction", 7.99)

    print(f"Added E-Book: {ebook1}")
    print(f"Added E-Book: {ebook2}")

    # Modifying e-book details
    ebook1.set_price(9.99)  # Assuming there's a method to set price
    print(f"Modified E-Book Price: {ebook1}")

    # Removing an e-book (simulate by not referencing it anymore)
    ebook1 = None
    print("Removed E-Book: 1984")


def test_add_modify_remove_customer():
    print("\nTesting Add/Modify/Remove Customer")

    # Adding a customer
    customer = Customer("Alice Smith", "+123456789", True, "alice.smith@example.com", "456 Oak St")
    print(f"Added Customer: {customer}")

    # Removing a customer (simulate by not referencing it anymore)
    customer = None
    print("Removed Customer: Alice Smith")


def test_shopping_cart_operations():
    print("\nTesting Shopping Cart Operations")

    # Creating e-books
    ebook1 = EBook("1984", "George Orwell", date(1949, 6, 8), "Dystopian", 8.99)
    printed_ebook1 = PrintedEBook("To Kill a Mockingbird", "Harper Lee", date(1960, 7, 11), "Fiction", 12.99,
                                   "Hardcover", 0.75, 2.99)  # Assuming format, weight, and shipping cost

    # Adding to shopping cart
    cart = ShoppingCart(cart_id="CART001")
    cart.add_item(ebook1)
    cart.add_item(printed_ebook1)
    print(f"Shopping Cart Total: {cart.get_total_price()}")  # Assuming this method returns the total price

    # Removing an item from the cart
    cart.remove_item(ebook1)
    print(f"Shopping Cart Total after removing an item: {cart.get_total_price()}")


def test_invoice_generation():
    print("\nTesting Invoice Generation")

    # Creating a shopping cart and customer
    cart = ShoppingCart(cart_id="CART001")
    ebook1 = EBook("1984", "George Orwell", date(1949, 6, 8), "Dystopian", 8.99)
    cart.add_item(ebook1)

    customer = Customer("Bob Brown", "+123456789", False, "bob.brown@example.com", "789 Pine St")

    # Creating an order
    order = Order(date.today(), cart.get_total_price(), "Processing", order_id="ORDER001")  # Assuming an order ID attribute

    # Creating an invoice
    invoice = Invoice(order, customer)  # Assuming this takes an order and customer
    print(invoice)


def test_payment_processing():
    print("\nTesting Payment Processing")

    # Creating a shopping cart, customer, and order
    cart = ShoppingCart(cart_id="CART002")
    ebook1 = EBook("1984", "George Orwell", date(1949, 6, 8), "Dystopian", 8.99)
    cart.add_item(ebook1)

    customer = Customer("Charlie Johnson", "+987654321", True, "charlie.johnson@example.com", "321 Maple St")
    order = Order(date.today(), cart.get_total_price(), "Processing", order_id="ORDER002")

    # Creating an invoice
    invoice = Invoice(order, customer)

    # Creating a payment
    payment = Payment(order, "Credit Card", order.get_amount())  # Assuming get_amount() returns the order amount
    print(payment)


def main():
    test_add_modify_remove_ebook()
    test_add_modify_remove_customer()
    test_shopping_cart_operations()
    test_invoice_generation()
    test_payment_processing()


if __name__ == "__main__":
    main()

