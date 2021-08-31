from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    job = models.CharField(max_length=40)

class Doctor(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    hid = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
    pid = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    did = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    disease = models.CharField(max_length=200)
    medical_comment = models.TextField()
    medtech_comment = models.TextField()

class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

class Treatment(models.Model):
    did = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    pid = models.ForeignKey(Patient, on_delete=models.CASCADE)
