# LETRA A - Listar todos os projetos com seus respectivos membros (Valor 0,2).
print('\nConsulta A')
from appprojetos.models import *
for projetos in Projeto.objects.all():
    membross = []
    for membro in projetos.membros.iterator():
        membross.append(membro.nome)
    print("Projeto:",projetos.titulo," Membros: ",membross)

# LETRA B - Listar todas as atividades que tenham sido executadas no mês de maio de 2015 (Valor 0,1).
print('\nConsulta B')
from appprojetos.models import *
for atividade in AtividadeProjeto.objects.filter(data_inicio__year=2015,  data_inicio__month=5).distinct():
        print("Atividade:",atividade.descricao)

# LETRA C - Listar todos as pessoas que fazem parte do Staff da Universidade cujo o nome começa com a letra A
print('\nConsulta C')
from appprojetos.models import *
for membro in Membro.objects.filter(nome__startswith='A'):
    print("Nome:",membro.nome)


# LETRA D - Listar o custo total de cada projeto (Valor 0,5 - Extra).
print('\nConsulta D')
from appprojetos.models import *
from django.db.models import Sum
query = AtividadeProjeto.objects.values('projeto').annotate(Valor=Sum('custo'))
for obj in query:
    print('O projeto %s custou R$ %.2f'%(Projeto.objects.get(id=obj['projeto']).titulo, obj['Valor']))

