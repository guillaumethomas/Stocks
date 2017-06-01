# python 3.6
from rtstock.stock import Stock
from datetime import date

def stocks_dict(stock_list):
    for s in stock_list:
        s['price'] = float(Stock(s['code']).get_latest_price()[0]['LastTradePriceOnly'])
        s['total_val'] = round(s['price'] * s['qty'],3)
    return stock_list

def total_value(stock_list):
    '''
    generate a list of dictionary:
    with the keys 'code', 'price','qty', 'tota_val'
    the last item is also a dictionary representing the value of the
    portfolio 'total_value'
    '''

    total = 0
    stock_list = stocks_dict(stock_list)
    for s in stock_list:
        total += s['total_val']
    stock_list.append(dict(total_value=total))
    return stock_list

def portfolio_string(stock_list):
    stock_list = total_value(stock_list)
    stock_only = stock_list[0:-1]

    intro = "Today %s\n" %(date.today())
    indiv_val = "\n | CODE | PRICE | QTY | TOTAL VALUE |\n"
    Summary = "\nTotal value of the portfolio is %s" % (stock_list[-1]['total_value'])

    for i in stock_only:
        stock_sentence = "| %s | %s |  %s |  %s | \n" % (i['code'], i['price'], i['qty'], i['total_val'])
        indiv_val += stock_sentence

    text = intro + indiv_val + Summary

    return text





