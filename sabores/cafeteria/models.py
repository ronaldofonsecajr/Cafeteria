from django.db import models

class Usuario(models.Model):
    pedido = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    celular = models.TextField(max_length=255, null=True, blank=True)
    endereco = models.TextField(max_length=255, null=True, blank=True)
    combo = models.CharField(max_length=255, null=True)

    
