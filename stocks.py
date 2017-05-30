# python 3.6

from rtstock.stock import Stock
# https://pypi.python.org/pypi/realtime-stock

def main():
    stock = Stock('JWN')
    a= stock.get_latest_price()[0]
    print(a)



if __name__ == "__main__":
    main()
