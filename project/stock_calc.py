# python 3.6
from rtstock.stock import Stock


def stocks_dict(stock_list):
    for s in stock_list:
        s['price'] = float(Stock(s['code']).get_latest_price()[0]['LastTradePriceOnly'])
        s['total_val'] = round(s['price'] * s['qty'],3)
    return stock_list

def total_value(stock_list):
    total = 0
    stock_list = stocks_dict(stock_list)
    for s in stock_list:
        total += s['total_val']
    stock_list.append(dict(total_value=total))
    return stock_list

#@app.route('/api/v1.0/tickers')



if __name__ == '__main__':
    app.run()