class Stock:
    def __init__(self,code, price, purchase_day, purchase_price, qty):
        self.code = code
        self.price = price
        self.purchase_day = purchase_day
        self.purchase_price = purchase_price
        self.qty = qty
            
class Portfolio:
    def __init__(self,owner, institution, stocks):
        self.owner = owner
        self.institution = institution
        self. stocks = stocks

