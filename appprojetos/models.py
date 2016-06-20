from django.db import models

# Create your models here.


class Projeto(models.Model):
    titulo = models.CharField("Título",max_length=256)
    data_inicio = models.DateField("Data de Início", null=False)
    data_termino = models.DateField("Data de Término", null=False)
    justificativa =  models.TextField("Justificativa")
    metodologia = models.TextField("Metodologia")
    resultados_esperados = models.TextField("Resultados Esperados")


class AtividadesProjeto(models.Model):
    descricao = models.CharField("Descrição", max_length=500)
    data_inicio = models.DateField("Data de Início", null=False)
    data_termino = models.DateField("Data de Término", null=False)
    custo = models.DecimalField("Custo",max_digits=20, decimal_places=2)
    projeto = models.ForeignKey(Projeto,on_delete=models.PROTECT, verbose_name="Projeto")



class Membros(models.Model):
    nome = models.CharField("Nome", max_length=250)
    cpf = models.CharField("CPF", max_length=11, unique=True)
    data_nascimento = models.DateField("Data de Nascimento", null=False)
    email = models.EmailField("E-Mail", max_length=200)
    telefone = models.CharField("Telefone", max_length=20)
    matricula = models.CharField("Matrícula", max_length=14, unique=True)


class MembrosProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT, verbose_name="Projeto")
    membro = models.ForeignKey(Membros, on_delete=models.PROTECT, verbose_name="Membro")
    unique_together = ('projeto', 'membro') #Unicidade para que o membro não esteja no mesmo projeto duas vezes