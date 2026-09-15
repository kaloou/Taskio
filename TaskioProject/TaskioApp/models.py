from django.db import models

class Projet(models.Model):
    
    nom = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    proprietaire = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projets'
    )

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('-date_creation', )


class Etiquette(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    couleur = models.CharField(max_length=7, default='#6c757d')  # code hex

    def __str__(self):
        return self.nom

class Tache(models.Model):
    STATUT_CHOICES = [
        ('a_faire', 'À faire'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
    ]
    PRIORITE_CHOICES = [
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='a_faire')
    priorite = models.CharField(max_length=10, choices=PRIORITE_CHOICES, default='moyenne')
    date_echeance = models.DateField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    projet = models.ForeignKey(
        Projet,
        on_delete=models.CASCADE,
        related_name='taches'
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='taches_assignees'
    )
    etiquettes = models.ManyToManyField(Etiquette, blank=True)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['date_echeance']