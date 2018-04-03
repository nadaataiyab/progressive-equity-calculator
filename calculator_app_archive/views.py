# To run:
# . venv/bin/activate  - gets you virtual environment
#$ export FLASK_APP=views.py
#export FLASK_DEBUG=1   - turns on debug
#$ flask run OR flask views.py if don't turn on virtual environment

from flask import Flask, url_for, render_template, request
from simple_pe_calculator import progressive_payout
import pandas as pd
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
    equity_holders_definitions = ['Name',
                                  'Equity Stake',
                                  'Subject to Progressive',
                                  'Triggered',
                                  'Employed',
                                  'Progressive Payout',
                                  'Standard Payout']

    message, pool, df_equity_holders = progressive_payout(exit_price, fin_independence, tax,
                                                      equity_names, equity_percent,
                                                       progressive, employed,
                                                       equity_holders_definitions)
    df_equity_holders = df_equity_holders[['Name',
                                           'Equity Stake',
                                           'Triggered',
                                           'Employed',
                                           'Standard Payout',
                                           'Progressive Payout']]

    return render_template('results.html',
                           exit_price=exit_price,
                           fi_num=fin_independence,
                           tax=(tax * 100),
                           message=message,
                           pool=pool,
                           equity_holders=df_equity_holders.to_html(col_space=100,
                                                                    index=False,
                                                                    justify='center' ))

#app.run(host="0.0.0.0", port=5000)
