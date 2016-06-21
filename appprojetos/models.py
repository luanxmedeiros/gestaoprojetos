from django.db import models

# Create your models here.


class Membro(models.Model):
    nome = models.CharField("Nome", max_length=250, null=False)
    cpf = models.CharField("CPF", max_length=11, unique=True, null=False)
    data_nascimento = models.DateField("Data de Nascimento", null=False)
    email = models.EmailField("E-Mail", max_length=200)
    telefone = models.CharField("Telefone", max_length=20)
    matricula = models.CharField("Matrícula", max_length=14, unique=True, null=False)


class Projeto(models.Model):
    titulo = models.CharField("Título",max_length=256, null=False)
    data_inicio = models.DateField("Data de Início", null=False)
    data_termino = models.DateField("Data de Término", null=False)
    justificativa =  models.TextField("Justificativa", null=False)
    metodologia = models.TextField("Metodologia", null=False)
    resultados_esperados = models.TextField("Resultados Esperados", null=False)
    #Relacionamento muitos para muitos
    membros = models.ManyToManyField(Membro, through="MembroProjeto")


class AtividadeProjeto(models.Model):
    descricao = models.CharField("Descrição", max_length=500)
    data_inicio = models.DateField("Data de Início", null=False)
    data_termino = models.DateField("Data de Término")
    custo = models.DecimalField("Custo",max_digits=20, decimal_places=2)
    projeto = models.ForeignKey(Projeto,on_delete=models.PROTECT, verbose_name="Projeto", null=False)


class MembroProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT, verbose_name="Projeto", null=False)
    membro = models.ForeignKey(Membro, on_delete=models.PROTECT, verbose_name="Membro", null=False)
    unique_together = ('projeto', 'membro') #Unicidade para que o membro não esteja no mesmo projeto duas vezes


class DesenvolvimentoAtividade(models.Model):
    estagio = models.CharField("Estágio", max_length=250, null=False)
    em_desenvolvimento = models.CharField("Desenvolvendo", max_length=250, null=False)
    atividade_projeto = models.ForeignKey(AtividadeProjeto, verbose_name="Atividade", null=False)
