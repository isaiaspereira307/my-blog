from django.db import models
from django.conf import settings
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.utils.timezone import now

class Post(models.Model):
    TOPICO = (
        ('Python','Python'),
        ('JavaScript','JavaScript'),
        ('Linux','Linux'),
        ('Hacking','Hacking'),
        ('BlockChain','BlockChain'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topico = models.CharField(max_length=12, choices=TOPICO)
    subtopico = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    post = models.TextField()
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicacao(self):
        self.data_publicacao = now()
        self.save()

    def __str__(self):
        return self.topico

    def get_absolute_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.pk})

class CasaRenataCourasForm(ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')





from django import forms


FREQUENCIA = (
    ('semanal','semanal'),
    ('quinzenal','quinzenal'),
    ('mensal','mesal'),
)


    


