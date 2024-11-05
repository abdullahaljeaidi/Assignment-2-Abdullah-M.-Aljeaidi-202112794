from datetime import date
from typing import List


class EBook:
    """Represents a standard e-book available in the digital store."""

    def __init__(self, title: str, author: str, publication_date: date, genre: str, price: float):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def set_title(self, title: str):
        """Sets the title of the e-book."""
        self.__title = title

    def get_title(self) -> str:
        """Returns the title of the e-book."""
        return self.__title

    def set_author(self, author: str):
        """Sets the author of the e-book."""
        self.__author = author

    def get_author(self) -> str:
        """Returns the author of the e-book."""
        return self.__author

    def set_publication_date(self, publication_date: date):
        """Sets the publication date of the e-book."""
        self.__publication_date = publication_date

    def get_publication_date(self) -> date:
        """Returns the publication date of the e-book."""
        return self.__publication_date

    def set_genre(self, genre: str):
        """Sets the genre of the e-book."""
        self.__genre = genre

    def get_genre(self) -> str:
        """Returns the genre of the e-book."""
        return self.__genre

    def set_price(self, price: float):
        """Sets the price of the e-book."""
        self.__price = price

    def get_price(self) -> float:
        """Returns the price of the e-book."""
        return self.__price

    def __str__(self) -> str:
        return f"EBook(title={self.__title}, author={self.__author}, publication_date={self.__publication_date}, genre={self.__genre}, price={self.__price})"


class PrintedEBook(EBook):
    """Represents a physical copy of an e-book."""

    def __init__(self, title: str, author: str, publication_date: date, genre: str, price: float,
                 print_format: str, shipping_weight: float, shipping_cost: float):
        super().__init__(title, author, publication_date, genre, price)
        self.__print_format = print_format
        self.__shipping_weight = shipping_weight
        self.__shipping_cost = shipping_cost

    def set_print_format(self, print_format: str):
        """Sets the format of the printed book."""
        self.__print_format = print_format

    def get_print_format(self) -> str:
        """Returns the print format of the book."""
        return self.__print_format

    def set_shipping_weight(self, shipping_weight: float):
        """Sets the shipping weight of the printed book."""
        self.__shipping_weight = shipping_weight

    def get_shipping_weight(self) -> float:
        """Returns the shipping weight of the printed book."""
        return self.__shipping_weight

    def set_shipping_cost(self, shipping_cost: float):
        """Sets the shipping cost of the printed book."""
        self.__shipping_cost = shipping_cost

    def get_shipping_cost(self) -> float:
        """Returns the shipping cost of the printed book."""
        return self.__shipping_cost

    def __str__(self) -> str:
        return (super().__str__() +
                f", PrintedEBook(print_format={self.__print_format}, shipping_weight={self.__shipping_weight}, shipping_cost={self.__shipping_cost})")


class ShoppingCart:
    """Manages a collection of e-books chosen by the customer for potential purchase."""

    def __init__(self, cart_id: str):
        self.__items: List[EBook] = []
        self.__total_price: float = 0.0
        self.__creation_date: date = date.today()
        self.__cart_id: str = cart_id

    def set_items(self, items: List[EBook]):
        """Sets the list of e-books in the cart."""
        self.__items = items
        self.calculate_total()

    def get_items(self) -> List[EBook]:
        """Returns the list of e-books in the cart."""
        return self.__items

    def set_total_price(self, total_price: float):
        """Sets the total price of the cart."""
        self.__total_price = total_price

    def get_total_price(self) -> float:
        """Returns the total price of the cart."""
        return self.__total_price

    def calculate_total(self):
        """Calculates the total price based on the items in the cart."""
        self.__total_price = sum(item.get_price() for item in self.__items)

    def add_item(self, book: EBook):
        """Adds an e-book to the cart."""
        self.__items.append(book)
        self.calculate_total()

    def remove_item(self, book: EBook):
        """Removes an e-book from the cart."""
        self.__items.remove(book)
        self.calculate_total()

    def set_creation_date(self, creation_date: date):
        """Sets the creation date of the cart."""
        self.__creation_date = creation_date

    def get_creation_date(self) -> date:
        """Returns the creation date of the cart."""
        return self.__creation_date

    def set_cart_id(self, cart_id: str):
        """Sets the cart's ID."""
        self.__cart_id = cart_id

    def get_cart_id(self) -> str:
        """Returns the cart's ID."""
        return self.__cart_id

    def __str__(self) -> str:
        items_str = ', '.join([str(item) for item in self.__items])
        return f"ShoppingCart(cart_id={self.__cart_id}, items=[{items_str}], total_price={self.__total_price}, creation_date={self.__creation_date})"


class Order:
    """Represents a finalized purchase with details on the order date, total amount, and status."""

    def __init__(self, order_date: date, amount: float, status: str, order_id: str):
        self.__order_date = order_date
        self.__amount = amount
        self.__status = status
        self.__order_id = order_id

    def set_order_date(self, order_date: date):
        """Sets the date of the order."""
        self.__order_date = order_date

    def get_order_date(self) -> date:
        """Returns the order date."""
        return self.__order_date

    def set_amount(self, amount: float):
        """Sets the order amount."""
        self.__amount = amount

    def get_amount(self) -> float:
        """Returns the order amount."""
        return self.__amount

    def set_status(self, status: str):
        """Sets the order status."""
        self.__status = status

    def get_status(self) -> str:
        """Returns the order status."""
        return self.__status

    def set_order_id(self, order_id: str):
        """Sets the order ID."""
        self.__order_id = order_id

    def get_order_id(self) -> str:
        """Returns the order ID."""
        return self.__order_id

    def __str__(self) -> str:
        return f"Order(order_date={self.__order_date}, amount={self.__amount}, status={self.__status}, order_id={self.__order_id})"


class Customer:
    """Stores information about customers, including personal details and loyalty membership status."""

    def __init__(self, name: str, contact: str, loyalty_member: bool, email: str, address: str):
        self.__name = name
        self.__contact = contact
        self.__loyalty_member = loyalty_member
        self.__email = email
        self.__address = address

    def set_name(self, name: str):
        """Sets the name of the customer."""
        self.__name = name

    def get_name(self) -> str:
        """Returns the name of the customer."""
        return self.__name

    def set_contact(self, contact: str):
        """Sets the contact information for the customer."""
        self.__contact = contact

    def get_contact(self) -> str:
        """Returns the contact information for the customer."""
        return self.__contact

    def set_loyalty_member(self, status: bool):
        """Sets the loyalty membership status for the customer."""
        self.__loyalty_member = status

    def is_loyalty_member(self) -> bool:
        """Returns the loyalty membership status of the customer."""
        return self.__loyalty_member

    def set_email(self, email: str):
        """Sets the email address of the customer."""
        self.__email = email

    def get_email(self) -> str:
        """Returns the email address of the customer."""
        return self.__email

    def set_address(self, address: str):
        """Sets the physical address of the customer."""
        self.__address = address

    def get_address(self) -> str:
        """Returns the physical address of the customer."""
        return self.__address

    def __str__(self) -> str:
        return (f"Customer(name={self.__name}, contact={self.__contact}, "
                f"loyalty_member={self.__loyalty_member}, email={self.__email}, address={self.__address})")


class Invoice:
    """Handles the details of invoices generated for customer orders."""

    def __init__(self, order: Order, customer: Customer):
        self.__order = order
        self.__customer = customer
        self.__invoice_date = date.today()
        self.__invoice_id = self.generate_invoice_id()

    def generate_invoice_id(self) -> str:
        """Generates a unique invoice ID."""
        return f"INV-{self.__invoice_date.strftime('%Y%m%d')}-{self.__order.get_order_id()}"

    def set_order(self, order: Order):
        """Sets the order associated with the invoice."""
        self.__order = order

    def get_order(self) -> Order:
        """Returns the order associated with the invoice."""
        return self.__order

    def set_customer(self, customer: Customer):
        """Sets the customer associated with the invoice."""
        self.__customer = customer

    def get_customer(self) -> Customer:
        """Returns the customer associated with the invoice."""
        return self.__customer

    def set_invoice_date(self, invoice_date: date):
        """Sets the date of the invoice."""
        self.__invoice_date = invoice_date

    def get_invoice_date(self) -> date:
        """Returns the date of the invoice."""
        return self.__invoice_date

    def set_invoice_id(self, invoice_id: str):
        """Sets the unique ID for the invoice."""
        self.__invoice_id = invoice_id

    def get_invoice_id(self) -> str:
        """Returns the unique ID for the invoice."""
        return self.__invoice_id

    def __str__(self) -> str:
        return (f"Invoice(invoice_id={self.__invoice_id}, invoice_date={self.__invoice_date}, "
                f"order={self.__order}, customer={self.__customer})")


class Payment:
    """Handles payment transactions for customer orders."""

    def __init__(self, order: Order, payment_method: str, amount: float):
        self.__order = order
        self.__payment_method = payment_method
        self.__amount = amount
        self.__payment_date = date.today()

    def set_order(self, order: Order):
        """Sets the order associated with the payment."""
        self.__order = order

    def get_order(self) -> Order:
        """Returns the order associated with the payment."""
        return self.__order

    def set_payment_method(self, payment_method: str):
        """Sets the payment method used for the transaction."""
        self.__payment_method = payment_method

    def get_payment_method(self) -> str:
        """Returns the payment method used for the transaction."""
        return self.__payment_method

    def set_amount(self, amount: float):
        """Sets the amount for the payment transaction."""
        self.__amount = amount

    def get_amount(self) -> float:
        """Returns the amount for the payment transaction."""
        return self.__amount

    def set_payment_date(self, payment_date: date):
        """Sets the date of the payment transaction."""
        self.__payment_date = payment_date

    def get_payment_date(self) -> date:
        """Returns the date of the payment transaction."""
        return self.__payment_date

    def __str__(self) -> str:
        return (f"Payment(order={self.__order}, payment_method={self.__payment_method}, "
                f"amount={self.__amount}, payment_date={self.__payment_date})")
