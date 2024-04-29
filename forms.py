from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import InputRequired, DataRequired

estados = {
    '1': ['DF', 'GO', 'MS', 'MT', 'TO'],
    '2': ['AC', 'AM', 'AP', 'PA', 'RO', 'RR'],
    '3': ['CE', 'MA', 'PI'],
    '4': ['AL', 'PB', 'PE', 'RN'],
    '5': ['BA', 'SE'],
    '6': ['MG'],
    '7': ['ES', 'RJ'],
    '8': ['SP'],
    '9': ['PR', 'SC'],
    '0': ['RS']
}
class GerarCPF(FlaskForm):
    sigla = SelectField('Estado', choices=[(estado, estado) for estado in sum(estados.values(), [])], validators=[InputRequired()])
    submit = SubmitField('Gerar')

class ValidarCPF(FlaskForm):
    cpf = StringField('CPF', validators= [DataRequired()])
    submit = SubmitField('Validar')
