from django.db import models

class Area_interesse(models.Model):
    """Classe Areas de interesse de notificação"""
    name = models.CharField(max_length=200, help_text='Adicione o nome do bairro que gostaria de receber notificações')

    def __str__(self):
        """String for representing the Model object."""
        return self.name