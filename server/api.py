from fastapi import FastAPI
from controller import *
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post('/votacao/{ID_chapa}/{ID_aluno}')
def votacao(ID_chapa, ID_aluno):
    voted = ControllerVotacao.cadastrar(ID_chapa=ID_chapa,ID_aluno=ID_aluno)
    return voted
@app.get('/login/{matricula}/{senha}')
def login(matricula, senha):
        response = ControllerAlunos.login(matricula=matricula, senha=senha)
        return response
@app.get('/votos')
def votos():
    quantAlunos = len(ControllerAlunos.ler())
    quantVotos = len(ControllerVotacao.ler())
    porcentagem = 100*(quantVotos/quantAlunos)
    return {'quantAlunos': quantAlunos, 'quantVotos': quantVotos, 'porcentagem': porcentagem}