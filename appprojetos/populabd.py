from appprojetos.models import *
# Criando projetos
proj01=Projeto(titulo='Proj1', data_inicio='06/19/2016', data_termino='',
               justificativa='Projeto de pesquisa', metodologia='pesquisa', resultados_esperados='conclusão da pesquisa')

proj02=Projeto(titulo='Proj1', data_inicio='06/20/2016', data_termino='',
               justificativa='Projeto de extensão', metodologia='pesquisa', resultados_esperados='Implantação do projeto')
proj01.save()
proj02.save()


# Criando atividades
ativ01 = AtividadesProjeto(descricao='Criar o cronograma',data_inicio='06/18/2016', data_termino='', custo='')
ativ02 = AtividadesProjeto(descricao='Obter informações sobre o assunto',data_inicio='06/19/2016', data_termino='', custo='')
ativ03 = AtividadesProjeto(descricao='Documentar o projeto',data_inicio='06/20/2016', data_termino='', custo='')
ativ01.save()
ativ02.save()
ativ03.save()


# Criando membros
membro01 = Membros(nome='Juliana', cpf='1234567891011',data_nascimento='01/01/1995',
                   email='juliana@email.com', telefone='9999-9990', matricula='20142148060154')

membro02 = Membros(nome='Luan', cpf='1234567891012',data_nascimento='01/01/1993',
                   email='luan@email.com', telefone='8888-8880', matricula='20142148060120')
membro01.save()
membro02.save()


