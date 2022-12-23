from django.db import models

class Registrace(models.Model):
    jmeno = models.CharField(verbose_name="Jméno", max_length=30)

    prijmeni = models.CharField(verbose_name="Přijmení", max_length=50)

    narozeni = models.DateField(verbose_name="Datum narození")

    uz_jmene = models.CharField(verbose_name="uzivatelske jmeno", max_length=30)

    heslo = models.CharField(verbose_name="heslo", max_length=100)

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name_plural = "Registrace"

    def __str__(self):
        return f"{self.prijmeni} {self.jmeno}"

class Trenink(models.Model):
    popis = models.CharField(verbose_name="popis_tréninku", max_length=300)

    datum = models.DateField(verbose_name="datum_konani_treninku")

    cas = models.TimeField(verbose_name="cas_konani_treninku")

    MISTA = (
        ("venku", "Venku"),
        ("mala_telocvicna", "Malá tělovična"),
        ("velka_telecvicna", "Velká tělocvična")
    )

    misto = models.CharField(choices=MISTA, verbose_name="misto_konani_treninku", max_length=20)

    class Meta:
        ordering = ['datum', 'cas']
        verbose_name_plural = "Trénink"

    def __str__(self):
        return f"{self.popis}: {self.datum}"