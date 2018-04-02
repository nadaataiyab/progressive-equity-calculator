from flask import Flask, url_for, render_template, request
from simple_pe_calculator import progressive_payout
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/payouts', methods=['POST'])
def results():
    exit_price = float(request.form['exit_price'])
    fin_independence = float(request.form['fi_num'])
    tax = float(request.form['tax'])
    equity_names = request.form['equity_names']
    equity_percent = request.form['equity_percent']
    progressive = request.form['progressive']
    employed = request.form['employed']
    
    message, pool, equity_holders = progressive_payout(exit_price, fin_independence, tax,
                                                      equity_names, equity_percent,
                                                       progressive, employed)

    return render_template('results.html',
                           exit_price=exit_price,
                           fi_num=fin_independence,
                           tax=tax,
                           equity_names=equity_names,
                           equity_percent=equity_percent,
                           progressive=progressive,
                           employed=employed,
                           message=message,
                           pool=pool,
                           equity_holders=equity_holders)

app.run(host="0.0.0.0", port=5000)