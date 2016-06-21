from appprojetos.models import *

# Criando membros
membro01=Membro(nome='Juliana',cpf='1234567891011',data_nascimento='1995-01-01', email='juliana@email.com', telefone='9999-9990', matricula='20152148030154')
membro02=Membro(nome='Luan',cpf='1234567891016',data_nascimento='1992-02-22', email='luan@email.com', telefone='8888-8880', matricula='20142190602129')
membro03=Membro(nome='André',cpf='1234567891652',data_nascimento='1993-03-18', email='andre@email.com', telefone='8888-8880', matricula='20142514806321')
membro04=Membro(nome='Anderson',cpf='1234567931012',data_nascimento='1993-04-14', email='anderson@email.com', telefone='8888-8880', matricula='20921482060123')
membro05=Membro(nome='Angela',cpf='1234567897112',data_nascimento='1993-05-22', email='angela@email.com', telefone='8888-8880', matricula='2014214090129')
membro06=Membro(nome='Paulo',cpf='1234567899412',data_nascimento='1993-06-19', email='paulo@email.com', telefone='8888-8880', matricula='20142134852123')
membro07=Membro(nome='Igor',cpf='1234567891012',data_nascimento='1993-07-18', email='igor@email.com', telefone='8888-8880', matricula='20172148060120')
membro08=Membro(nome='Antônio',cpf='1234567601012',data_nascimento='1993-08-12', email='antonio@email.com', telefone='8888-8880', matricula='20149588060127')
membro09=Membro(nome='Fernando',cpf='1234564191012',data_nascimento='1993-09-11', email='fernando@email.com', telefone='8888-8880', matricula='20323148060120')
membro10=Membro(nome='Carlos',cpf='1234567898012',data_nascimento='1993-10-21', email='carlos@email.com', telefone='8888-8880', matricula='201432146560120')
membro01.save()
membro02.save()
membro03.save()
membro04.save()
membro05.save()
membro06.save()
membro07.save()
membro08.save()
membro09.save()
membro10.save()

# Criando projetos
proj01=Projeto(titulo='Proj1', data_inicio='2015-02-10', data_termino='',justificativa='Projeto de pesquisa', metodologia='pesquisa', resultados_esperados='conclusão da pesquisa')
proj02=Projeto(titulo='Proj1', data_inicio='2015-01-21', data_termino='',justificativa='Projeto de extensão', metodologia='pesquisa', resultados_esperados='Implantação do projeto')


#Adicionando membros aos projetos
proj01.membros.add(membro01,membro02,membro03,membro04,membro05)
proj02.membros.add(membro06,membro07,membro08,membro09,membro10)

proj01.save()
proj02.save()

# Criando atividades
ativ01=Atividade(descricao='Criar o cronograma',data_inicio='2016-06-18', data_termino='', custo=2216.9)
ativ02=Atividade(descricao='Obter informações sobre o assunto',data_inicio='2016-06-19', data_termino='', custo=2000.1)
ativ03=Atividade(descricao='Documentar o projeto',data_inicio='2016-06-20', data_termino='', custo=1231.2)
ativ04=Atividade(descricao='Levantar Requisitos',data_inicio='2016-06-20', data_termino='', custo=1110.0)


#Associando atividades aos projetos
ativ01.projeto.add(proj01)
ativ02.projeto.add(proj01)
ativ03.projeto.add(proj02)
ativ04.projeto.add(proj02)

ativ01.save()
ativ02.save()
ativ03.save()
ativ03.save()

desenv1 = DesenvolvimentoAtividade(estagio='Reunião com a equipe', em_desenvolvimento='Debate sobre as necessidades dos cliente',atividade_projeto=ativ01)
desenv2 = DesenvolvimentoAtividade(estagio='Refatoração de código', em_desenvolvimento='Reduzindo o número de variáveis desnecessárias',atividade_projeto=ativ03)
desenv1.save()
desenv2.save()