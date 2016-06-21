'''
a. Listar todos os projetos com seus respectivos membros (Valor 0,2).
b. Listar todas as atividades que tenham sido executadas no mês de maio de 2015 (Valor 0,1).
c. Listar todos as pessoas que fazem parte do Staff da Universidade cujo o nome começa com a letra A (Valor 0,2)
d. Listar o custo total de cada projeto (Valor 0,5 - Extra).
'''

# LETRA A
# LETRA B
# LETRA C
from appprojetos.models import *
for membro in Membro.objects.filter(nome__startswith='L'):
    print("Nome:",membro.nome)

# LETRA D
