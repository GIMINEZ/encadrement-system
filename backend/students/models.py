# from django.db import models
from django.db import models
from users.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")

    matricule = models.CharField(max_length=50, unique=True)
    numero_bac = models.CharField(max_length=50, blank=True, null=True)
    nni = models.CharField(max_length=50, blank=True, null=True)
    sexe = models.CharField(max_length=1, choices=[("M", "Homme"), ("F", "Femme")])
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=200, blank=True, null=True)
    nationalite = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return f"{self.matricule} - {self.prenom} {self.nom}"


class StudentContact(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="contact")
    email_pro = models.EmailField(blank=True, null=True)
    email_perso = models.EmailField(blank=True, null=True)
    tel1 = models.CharField(max_length=20, blank=True, null=True)
    tel2 = models.CharField(max_length=20, blank=True, null=True)
    tel_parent1 = models.CharField(max_length=20, blank=True, null=True)
    tel_parent2 = models.CharField(max_length=20, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)


class StudentHealth(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="health")
    groupe_sanguin = models.CharField(max_length=5, blank=True, null=True)
    assureur = models.CharField(max_length=100, blank=True, null=True)
    num_assure = models.CharField(max_length=50, blank=True, null=True)
    antecedents = models.TextField(blank=True, null=True)
    maladies_chroniques = models.TextField(blank=True, null=True)
    poids = models.FloatField(blank=True, null=True)
    taille = models.FloatField(blank=True, null=True)
    imc = models.FloatField(blank=True, null=True)


class StudentAcademic(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="academic")
    departement = models.CharField(max_length=100, blank=True, null=True)
    niveau_actuel = models.CharField(max_length=50, blank=True, null=True)
    semestre = models.CharField(max_length=20, blank=True, null=True)
    annee_s1 = models.IntegerField(blank=True, null=True)
    validation_s1 = models.BooleanField(default=False)
    releve_s1 = models.FileField(upload_to="documents/academics/", blank=True, null=True)
    attestation_s1 = models.FileField(upload_to="documents/academics/", blank=True, null=True)


class StudentMilitary(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="military")
    compagnie = models.CharField(max_length=50, blank=True, null=True)
    section = models.CharField(max_length=50, blank=True, null=True)
    sport = models.CharField(
        max_length=50,
        choices=[
            ("foot", "Football"),
            ("course", "Course"),
            ("marche", "Marche"),
            ("natation", "Natation"),
            ("voley", "Volley"),
            ("aucun", "Pas de sport"),
        ],
        default="aucun"
    )


class StudentClothing(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="clothing")
    taille = models.FloatField(blank=True, null=True)
    tour_poitrine = models.FloatField(blank=True, null=True)
    tour_ceinture = models.FloatField(blank=True, null=True)
    tour_taille = models.FloatField(blank=True, null=True)
    tour_bassin = models.FloatField(blank=True, null=True)
    tour_cou = models.FloatField(blank=True, null=True)
    longueur_manche = models.FloatField(blank=True, null=True)
    longueur_dos = models.FloatField(blank=True, null=True)
    longueur_cote = models.FloatField(blank=True, null=True)
    pointure = models.FloatField(blank=True, null=True)


class StudentHousing(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="housing")
    batiment = models.CharField(max_length=50, blank=True, null=True)
    etage = models.CharField(max_length=20, blank=True, null=True)
    aile = models.CharField(max_length=20, blank=True, null=True)
    chambre = models.CharField(max_length=20, blank=True, null=True)
    lit = models.CharField(max_length=20, blank=True, null=True)
    responsable_chambre = models.BooleanField(default=False)
    responsable_aile = models.BooleanField(default=False)
    responsable_etage = models.BooleanField(default=False)


class StudentDocument(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="documents")
    type_document = models.CharField(
        max_length=50,
        choices=[
            ("cin", "Carte d'identité"),
            ("naissance", "Acte de naissance"),
            ("bac", "Diplôme du Bac"),
            ("licence", "Diplôme Licence"),
            ("photo1", "Photo militaire"),
            ("photo2", "Photo civile"),
            ("photo3", "Photo militaire intégrale"),
            ("autre", "Autre"),
        ]
    )
    fichier = models.FileField(upload_to="documents/students/")
    date_upload = models.DateTimeField(auto_now_add=True)

# Create your models here.
