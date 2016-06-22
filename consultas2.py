
# LETRA A - Listar todos os projetos com seus respectivos membros (Valor 0,2).
from appprojetos.models import *
'''
for projetos in Projeto.objects.all():
    membross = []
    for membro in projetos.membros.iterator():
        membross.append(membro.nome)
    print("Projeto:",projetos.titulo," Membros: ",membross)

# LETRA B - Listar todas as atividades que tenham sido executadas no mês de maio de 2015 (Valor 0,1).
from appprojetos.models import *
for atividade in AtividadeProjeto.objects.filter(data_inicio__year=2015,  data_inicio__month=5).distinct():
        print("Atividade:",atividade.descricao)


# LETRA C - Listar todos as pessoas que fazem parte do Staff da Universidade cujo o nome começa com a letra A
from appprojetos.models import *
for membro in Membro.objects.filter(nome__startswith='A'):
    print("Nome:",membro.nome)


# LETRA D - Listar o custo total de cada projeto (Valor 0,5 - Extra).
from appprojetos.models import *
for custo in AtividadeProjeto.custo():
    print("Custo:",custo)
'''


from appprojetos.models import *
from django.db.models import Sum

'''
lista = AtividadeProjeto.objects.annotate(Sum('custo')).values('custo__sum', 'projeto') group by
for x in lista:
    x.custo
'''
#MAIS OU MENOS BOM
#print(AtividadeProjeto.objects.values('projeto').annotate(Valor=Sum('custo')))
#print(AtividadeProjeto.objects.values('projeto').annotate(Custo_Total=Sum('custo')))

query = AtividadeProjeto.objects.values('projeto').annotate(Valor=Sum('custo'))
for x in range(len(query)):
    obj = query[x]
    print('O projeto %s custou R$ %.2f'%(Projeto.objects.get(id=obj['projeto']).titulo, obj['Valor']))