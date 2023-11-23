from flask import Flask, render_template, request, redirect


app = Flask(__name__)


class cadinflu:
    def __init__(self, nome, plataformas, seguidores, interesse):
        self.nome = nome
        self.plataformas = plataformas
        self.seguidores = seguidores
        self.interesse = interesse

lista = []

@app.route('/')
def hello_world():
    return 'começando!'


@app.route('/influence')
def influence():
    return render_template('influen.html', Titulo="Os influencers: ", ListaInfluence =lista)

@app.route('/cadrastroinflu')
def cadrastroinflu():
    return render_template('cadrastroinflu.html', Titulo = "Cadastro de influencers")


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    plataformas = request.form['plataformas']
    seguidores = request.form['seguidores']
    interesse = request.form['interesse']
    obj = cadinflu(nome,plataformas,seguidores,interesse)
    lista.append(obj)
    return redirect('/influence')


if __name__ == '__main__':
    app.run()
