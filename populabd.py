from appprojetos.models import *

# Criando membros
membro01=Membro(nome='Juliana',cpf='1234567891011',data_nascimento='1995-01-01', email='juliana@email.com', telefone='9999-9990', matricula='20142148060154')
membro02=Membro(nome='Luan',cpf='1234567891012',data_nascimento='1993-01-01', email='luan@email.com', telefone='8888-8880', matricula='20142148060120')
membro01.save()
membro02.save()

# Criando projetos
proj01=Projeto(titulo='Proj1', data_inicio='2015-02-10', data_termino='',justificativa='Projeto de pesquisa', metodologia='pesquisa', resultados_esperados='conclusão da pesquisa')
proj02=Projeto(titulo='Proj1', data_inicio='2015-01-21', data_termino='',justificativa='Projeto de extensão', metodologia='pesquisa', resultados_esperados='Implantação do projeto')
proj01.save()
proj02.save()

# Criando atividades
ativ01=AtividadeProjeto(descricao='Criar o cronograma',data_inicio='2016-06-18', data_termino='', custo='')
ativ02=AtividadeProjeto(descricao='Obter informações sobre o assunto',data_inicio='2016-06-19', data_termino='', custo='')
ativ03=AtividadeProjeto(descricao='Documentar o projeto',data_inicio='2016-06-20', data_termino='', custo='')
ativ01.save()
ativ02.save()
ativ03.save()
