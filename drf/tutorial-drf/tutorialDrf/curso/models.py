# from django.db import models, CheckConstraint, Q
from django.db import models

# Create your models here.
class Base(models.Model):
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=200)
    url = models.URLField(unique=True)

    class Meta:
        db_table = 'curso'
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.titulo
    

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario  = models.TextField(blank=True, default="")
    avaliacao = models.PositiveIntegerField()
    teste = models.CharField(max_length=255)
    class Meta:
        db_table = 'avaliacao'
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        unique_together = ["email", "curso"]

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota = {self.avaliacao}'