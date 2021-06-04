from django.db import models


class Artist(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)

    class Meta:
        verbose_name = "auteur"

    def __str__(self):
        return self.name
  

class Contact(models.Model):
    email = models.EmailField('email', max_length=100)
    name = models.CharField('nom', max_length=200)
    
    class Meta:
            verbose_name = "prospect"    
    
    def __str__(self):
        return self.name


class Oeuvre(models.Model):
    reference = models.IntegerField('référence', blank=True, null=True)
    create_at = models.DateTimeField('date de création', auto_now_add=True)
    available = models.BooleanField('disponible',default=True)
    title = models.CharField('titre', max_length=200)
    picture = models.URLField("URL de l'image")
    auteurs = models.ManyToManyField(Artist, related_name='oeuvres', blank=True)
    
    class Meta:
            verbose_name = "oeuvre"
    
    def __str__(self):
        return self.title



class Booking(models.Model):
    created_at = models.DateTimeField("date d'envoi", auto_now_add=True)
    contacted = models.BooleanField('demande traitée ?', blank=True, default=False)
    album = models.OneToOneField(Oeuvre, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "réservation"

    def __str__(self):
        return self.contact.name
