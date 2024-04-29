from flask import Flask, render_template, request
import random
from forms import GerarCPF, ValidarCPF

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    cpf = None
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

    form = GerarCPF()

    if form.validate_on_submit():
        sigla = form.sigla.data

        if sigla in sum(estados.values(), []):
            d1 = random.randint(0, 9)
            d2 = random.randint(0, 9)
            d3 = random.randint(0, 9)
            d4 = random.randint(0, 9)
            d5 = random.randint(0, 9)
            d6 = random.randint(0, 9)
            d7 = random.randint(0, 9)
            d8 = random.randint(0, 9)

            num9 = None
            for num, estado in estados.items():
                if sigla in estado:
                    num9 = num
                    break

            if num9 is not None:
                d9 = int(num9)

                calc1 = (10 * d1) + (9 * d2) + (8 * d3) + (7 * d4) + (6 * d5) + (5 * d6) + (4 * d7) + (3 * d8) + (2 * d9)
                rest1 = calc1 % 11

                if rest1 == 0 or rest1 == 1:
                    d10 = 0
                else:
                    d10 = 11 - rest1

                calc2 = (10 * d2) + (9 * d3) + (8 * d4) + (7 * d5) + (6 * d6) + (5 * d7) + (4 * d8) + (3 * d9) + (4 * d10)
                rest2 = calc2 % 11

                if rest2 == 0 or rest2 == 1:
                    d11 = 0
                else:
                    d11 = 11 - rest2

                cpf = f'{d1}{d2}{d3}.{d4}{d5}{d6}.{d7}{d8}{d9}-{d10}{d11}'
            else:
                return 'Insira a Sigla Corretamente'
    
    return render_template('index.html', form=form, cpf=cpf, p_atual ='gera')

@app.route('/outra-rota', methods = [ 'GET', 'POST'])
def outra_rota():
    form = ValidarCPF()
    cpf = None
    mensagem = ''
    cpf_gerado= None
    cpf_final = None
    if form.validate_on_submit():
        cpf = form.cpf.data 
        cpf = cpf.replace(".", "")
        cpf = cpf.replace( "-","")
        cpf_final = cpf
        if not cpf_final.isdigit() or len(cpf_final) != 11:
            mensagem = 'CPF digitado incorretamente'
        else:
            NoveD = cpf[:9]
            cont1 = 10
            resultado1 = resultado2 = 0
            for digito in NoveD:
                resultado1 += int(digito)*cont1
                cont1 -= 1

            PrDigito = (resultado1*10) % 11

            PrDigito = PrDigito if PrDigito <= 9 else 0 

            DezD = NoveD + str(PrDigito)
            cont2 = 11

            for digito in DezD:
                resultado2 += int(digito)*cont2
                cont2 -= 1
                
            SegDigito = (resultado2*10) % 11
            SegDigito = SegDigito if SegDigito <= 9 else 0 

            cpf_gerado = f'{NoveD}{PrDigito}{SegDigito}'
            print(cpf_gerado)

    return render_template('validandocpf.html', form=form, cpf_final=cpf_final, cpf_gerado= cpf_gerado, mensagem=mensagem, p_atual = 'valida') 

if __name__ == '__main__':
    app.run(debug=True)
