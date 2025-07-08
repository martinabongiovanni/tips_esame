from dataclasses import dataclass


@dataclass
class Stock:
    stock_id: int
    product_id: int
    quantity: int

    def __hash__(self):
        return hash((self.stock_id, self.product_id))

    def __eq__(self, other):
        if isinstance(other, Stock):
            return self.stock_id == other.stock_id and self.product_id == other.product_id
        return False

    def __lt__(self, other):
        return self.stock_id < other.order_id

    def __str__(self):
        return f"{self.stock_id} - {self.product_id}"