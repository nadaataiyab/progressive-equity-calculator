from flask import Flask, url_for, render_template, request
from simple_pe_calculator import progressive_payout
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/payouts', methods=['POST'])
def results():
    exit_price = request.form['exit_price']
    fi_num = request.form['fi_num']
    tax = request.form['tax']
    equity_names = request.form['equity_names']
    equity_percent = request.form['equity_percent']
    progressive = request.form['progressive']
    employed = request.form['employed']

    return render_template('results.html',
                           exit_price=exit_price,
                           fi_num=fi_num,
                           tax=tax,
                           equity_names=equity_names,
                           equity_percent=equity_percent,
                           progressive=progressive,
                           employed=employed)
