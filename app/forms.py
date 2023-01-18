from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class NameInputForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit_name = SubmitField('OK')
class DeleteDatabaseForm(FlaskForm):
    submit_delete = SubmitField('Delete Database')
class LetterForm(FlaskForm):
    letter = SelectField('letter',
                        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'),
                                 ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'),
                                 ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'),
                                 ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], default='A')
    letter_submit = SubmitField('Filter')
