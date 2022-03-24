from fastapi import FastAPI
from controller import *

app = FastAPI()

KEY = 'alVG34uf87'

@app.post(f'{KEY}/votacao')
def votacao(ID_chapa, ID_aluno):
    voted = ControllerVotacao.cadastrar(ID_chapa=ID_chapa,ID_aluno=ID_aluno)
    return voted

@app.post(f'{KEY}/login')
def login(matricula, senha):
    response = ControllerAlunos.login(matricula=matricula, senha=senha)
    return response

@app.post(f'{KEY}/votos')
def votos():
    quantAlunos = len(ControllerAlunos.ler())
    quantVotos = len(ControllerVotacao.ler())
    porcentagem = 100*(quantVotos/quantAlunos)
    return {'quantAlunos': quantAlunos, 'quantVotos': quantVotos, 'porcentagem': porcentagem}