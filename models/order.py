class Order():

    def __init__(self, customer_name, order_date, description, qty, price):
        self.customer_name = customer_name
        self.order_date = order_date
        self.description = description
        self.qty = qty
        self.price = price
        self.total_price = float(self.qty) * float(self.price)

