from appprojetos.models import *

membro01=Membro(nome='Juliana',cpf='1234567891011',data_nascimento='1995-01-01', email='juliana@email.com', telefone='9999-9990', matricula='20152148030154')
membro02=Membro(nome='Luan',cpf='1234567891016',data_nascimento='1992-02-22', email='luan@email.com', telefone='8888-8880', matricula='20142190602129')
membro03=Membro(nome='André',cpf='1234567891652',data_nascimento='1993-03-18', email='andre@email.com', telefone='8888-8880', matricula='20142514806321')
membro01.save()
membro02.save()
membro03.save()



# Criando projetos
proj01=Projeto(titulo='Proj1', data_inicio='2015-02-10', data_termino='',justificativa='Projeto de pesquisa', metodologia='pesquisa', resultados_esperados='conclusão da pesquisa')
proj02=Projeto(titulo='Proj1', data_inicio='2015-01-21', data_termino='',justificativa='Projeto de extensão', metodologia='pesquisa', resultados_esperados='Implantação do projeto')

proj01.save()
proj02.save()

proj01.membros.add(membro01,membro02)
proj01.membros.add(membro03)

# Criando atividades
ativ01=AtividadeProjeto(descricao='Criar o cronograma',data_inicio='2016-06-18', data_termino='', custo=2216.9,projeto=proj01)
ativ02=AtividadeProjeto(descricao='Obter informações sobre o assunto',data_inicio='2016-06-19', data_termino='', custo=2000.1,projeto=proj01)
ativ03=AtividadeProjeto(descricao='Documentar o projeto',data_inicio='2016-06-20', data_termino='', custo=1231.2,projeto=proj02)
ativ04=AtividadeProjeto(descricao='Levantar Requisitos',data_inicio='2016-06-20', data_termino='', custo=1110.0,projeto=proj02)

ativ01.save()
ativ02.save()
ativ03.save()
ativ03.save()

'''
desenv1 = DesenvolvimentoAtividade(estagio='Reunião com a equipe', em_desenvolvimento='Debate sobre as necessidades dos cliente',atividade_projeto=ativ01)
desenv2 = DesenvolvimentoAtividade(estagio='Refatoração de código', em_desenvolvimento='Reduzindo o número de variáveis desnecessárias',atividade_projeto=ativ03)
desenv1.save()
desenv2.save()
'''