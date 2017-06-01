# python 3.6
from flask import Flask, jsonify
from portfolio import portfolio
from stock_calc import total_value, portfolio_string



app = Flask(__name__)


#@app.route('/api/v1.0/tickers')
@app.route('/')
def index():
    a = jsonify(total_value(portfolio()))
    b = portfolio_string(portfolio())
    #print(a)
    return a, b


if __name__ == '__main__':
    app.debug = True
    app.run()