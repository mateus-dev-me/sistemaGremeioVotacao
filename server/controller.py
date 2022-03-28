from session import retornaSession
import hashlib
from model import *
class ControllerAlunos:
    #Cadastro
    @classmethod
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
    '''
    Login

    Return:
    Aluno - Matrícula e senha corretos.
    2 - Matrícula e/ou senha incorretos.

    '''
    @classmethod
    def login(cls, matricula, senha):
        senha = hashlib.sha256(senha.encode()).hexdigest()
        session =  retornaSession()
        existeMatricula = session.query(Alunos).filter(Alunos.matricula == matricula).all()
        if len(existeMatricula) == 1 and existeMatricula[0].senha == senha:
            return {'ID_aluno': existeMatricula[0].id}
        else:
            return {'status': 2}
    @classmethod
    # Ler
    def ler(cls):
        session =  retornaSession()
        alunos = session.query(Alunos).all()
        return alunos
class ControllerChapas:
    # Cadastro
    @classmethod
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
    # Ler
    @classmethod
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
    '''
    Votação

    Return:
    Chapa - voto confirmado.
    2 - Erro interno do sistema.
    3 - Chapa ou aluno inexistente.
    4 - Aluno já votou.

    '''
    @classmethod
    def cadastrar(cls, ID_chapa, ID_aluno):
        session =  retornaSession()
        existeChapa = session.query(Chapas).filter(Chapas.id == ID_chapa).all()
        existeVoto = session.query(AlunosVot).filter(AlunosVot.ID_aluno == ID_aluno).all()
        existeAluno = session.query(Alunos).filter(Alunos.id == ID_aluno).all()
        if len(existeVoto) == 0:
            if len(existeChapa) > 0 and len(existeAluno) == 1:
                try:
                    newVot = Votacao(ID_chapa = ID_chapa)
                    session.add(newVot)
                    session.commit()
                    newAlunoVot = AlunosVot(ID_aluno = ID_aluno)
                    session.add(newAlunoVot)
                    session.commit()
                    return {'chapa': existeChapa[0].id}
                except:
                    return 2
            else:
                return 3
        else:
            return 4
    # Ler
    @classmethod
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