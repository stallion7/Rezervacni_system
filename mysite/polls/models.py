from django.db import models

class Registrace(models.Model):
    jmeno = models.CharField(verbose_name="Jméno", max_length=30)

    prijmeni = models.CharField(verbose_name="Přijmení", max_length=50)

    narozeni = models.DateField(verbose_name="Datum narození")

    uz_jmene = models.CharField(verbose_name="uzivatelske jmeno", max_length=30)

    heslo = models.CharField(verbose_name="heslo", max_length=100)

    class Meta:
        ordering = ['prijmeni', 'jmeno']

    def __str__(self):
        return f"{self.prijmeni} {self.jmeno}"