from model import *
from session import retornaSession
import hashlib
class ControllerAlunos:
    @classmethod
    # Cadastro
    def cadastrar(cls, matricula, senha, nome):
        session =  retornaSession()
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            newAluno = Alunos(matricula = matricula, senha = senha, nome = nome)
            session.add(newAluno)
            session.commit()
            return 1
        except:
            return 2
    @classmethod
    # Login
    def login(cls, matricula, senha):
        senha = hashlib.sha256(senha.encode()).hexdigest()
        session =  retornaSession()
        existeMatricula = session.query(Alunos).filter(Alunos.matricula == matricula).all()
        if len(existeMatricula) == 1 and existeMatricula[0].senha == senha:
            return existeMatricula[0]
        else:
            return 2
    @classmethod
    # Ler
    def ler(cls):
        session =  retornaSession()
        alunos = session.query(Alunos).all()
        return alunos
class ControllerChapas:
    @classmethod
    # Cadastro
    def cadastrar(cls, numero, ID_presidente, ID_vice):
        session =  retornaSession()
        existePesidente = session.query(Alunos).filter(Alunos.id == ID_presidente).all()
        existeVice = session.query(Alunos).filter(Alunos.id == ID_vice).all()
        if len(existePesidente) > 0 and len(existeVice) > 0:
            try:
                newChapa = Chapas(numero = numero, ID_presidente = ID_presidente, ID_vice = ID_vice)
                session.add(newChapa)
                session.commit()
                return 1
            except:
                return 2
        else:
            print('ID não encontrado(s).')
    @classmethod
    # Ler
    def ler(cls):
        session =  retornaSession()
        chapasBD = session.query(Chapas).all()
        chapas = []
        for chapa in chapasBD:
            presidente = session.query(Alunos).filter(Alunos.id == chapa.ID_presidente).all()
            vice = session.query(Alunos).filter(Alunos.id == chapa.ID_vice).all()
            chapas.append({'numero': chapa.numero, 'presidente': presidente[0].nome, 'vice': vice[0].nome})
        return chapas
class ControllerVotacao:
    @classmethod
    # Cadastro
    def cadastrar(cls, ID_chapa, ID_aluno):
        session =  retornaSession()
        existeChapa = session.query(Chapas).filter(Chapas.id == ID_chapa).all()
        existeVoto = session.query(AlunosVot).filter(AlunosVot.ID_aluno == ID_aluno).all()
        if len(existeVoto) == 0:
            if len(existeChapa) > 0:
                try:
                    newVot = Votacao(ID_chapa = ID_chapa)
                    session.add(newVot)
                    session.commit()
                    newAlunoVot = AlunosVot(ID_aluno = ID_aluno)
                    session.add(newAlunoVot)
                    session.commit()
                    return existeChapa
                except:
                    return 2
            else:
                return 3
        else:
            return 4
    @classmethod
    # Ler
    def ler(cls):
        session =  retornaSession()
        chapasBD = session.query(Chapas).all()
        chapas = []
        for chapa in chapasBD:
            votos = session.query(Votacao).filter(Votacao.ID_chapa == chapa.id).all()
            presidente = session.query(Alunos).filter(Alunos.id == chapa.ID_presidente).all()
            vice = session.query(Alunos).filter(Alunos.id == chapa.ID_vice).all()
            chapas.append({'votos': len(votos), 'numero': chapa.numero, 'presidente': presidente[0].nome, 'vice': vice[0].nome})
        return chapas

a = ControllerAlunos()
c = ControllerChapas()
v = ControllerVotacao()