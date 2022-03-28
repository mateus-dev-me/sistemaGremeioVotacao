from fastapi import FastAPI
from controller import *
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()
origins = ['http://127.0.0.1:5500']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post('/votacao')
def votacao(ID_chapa:int, ID_aluno:int):
    voted = ControllerVotacao.cadastrar(ID_chapa=ID_chapa,ID_aluno=ID_aluno)
    return voted
@app.post('/login')
def login(matricula:int, senha:str):
        response = ControllerAlunos.login(matricula=matricula, senha=senha)
        return response
@app.get('/votos')
def votos():
    quantAlunos = len(ControllerAlunos.ler())
    quantVotos = len(ControllerVotacao.ler())
    porcentagem = 100*(quantVotos/quantAlunos)
    return {'quantAlunos': quantAlunos, 'quantVotos': quantVotos, 'porcentagem': porcentagem}
if __name__ == '__main__':
    uvicorn.run('api:app', port=5000, reload=True, access_log=False)