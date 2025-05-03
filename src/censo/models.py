from django.db import models

class DadosCenso(models.Model):
    nome = models.CharField(max_length=100)
    conteudo = models.TextField()
    categorias = models.TextField()
    
  
    

    def __str__(self):
        return self.nome
    

# Create your models here.
