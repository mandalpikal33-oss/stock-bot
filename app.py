from flask import Flask, Response, request
import yfinance as yf

app = Flask(__name__)

@app.route('/get-stock-price', methods=['GET', 'POST'])
def get_stock_price():
    ticker_symbol = request.args.get('ticker', 'AAPL')
    
    try:
        stock = yf.Ticker(ticker_symbol)
        todays_data = stock.history(period='1d')
        if not todays_data.empty:
            current_price = round(todays_data['Close'].iloc[-1], 2)
            text_to_play = f"מחיר מניית {ticker_symbol} הוא {current_price} דולר."
        else:
            text_to_play = f"לא ניתן כרגע לקבל את נתוני המניה עבור {ticker_symbol}."
    except Exception as e:
        text_to_play = "אירעה שגיאה בשליפת הנתונים."

    response_text = f"t2s={text_to_play}"
    return Response(response_text, mimetype='text/plain; charset=utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)