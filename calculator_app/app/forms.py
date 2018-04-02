from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, DecimalField

Class InputForm(FlaskForm):
    exit_price = FloatField('Exit Price', validators=[DataRequired()])
    fin_independence = FloatField('Financial Independence Number', validators=[DataRequired()])
    tax = DecimalField('Equity Tax', validators=[DataRequired()])
