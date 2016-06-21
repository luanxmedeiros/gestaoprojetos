
# LETRA A - Listar todos os projetos com seus respectivos membros (Valor 0,2).
from appprojetos.models import *
for projetos in Projeto.objects.all():
    print("Projeto:",projetos.titulo,"Membros:",membro.nome)
'''
# LETRA B - Listar todas as atividades que tenham sido executadas no mês de maio de 2015 (Valor 0,1).

# LETRA C - Listar todos as pessoas que fazem parte do Staff da Universidade cujo o nome começa com a letra A (Valor 0,2)
from appprojetos.models import *
for membro in Membro.objects.filter(nome__startswith='L'):
    print("Nome:",membro.nome)

# LETRA D - Listar o custo total de cada projeto (Valor 0,5 - Extra).
from appprojetos.models import *
for custo in AtividadeProjeto.custo():
    print("Custo:",AtividadeProjeto.custo)
'''