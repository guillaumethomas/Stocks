from rtstock.stock import Stock
from flask import Flask, jsonify

app = Flask(__name__)


#@app.route('/api/v1.0/tickers')
@app.route('/')
def index():
    stock = Stock('JWN')
    s = stock.get_latest_price()[0]
    #return jsonify(dict(JWN=s['LastTradePriceOnly']))
    return "Hello"

if __name__ == '__main__':
    app.run()