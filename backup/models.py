from django.db import models

# Create your models here.


"""This model will contain the medical entry of an user"""
"""Entries:
            - Gender
            - Age
            - Race/Ethicity
            - Diagnosis
            - MD
            - Assignment
            - EMR
            - RAR
            - LOS
            - A
            - B
            - C
            - D
            - E
            - F
            - G
            - H
            - I
            - J
            - K
            - L
            - M
            - N
            - O
            - P
            - Q
            - R
            - S
            - T
            - U
            - V
            - W
            - X
            - Y
            - Z
            - AA
            - AB
            - AC
            - AD
            - #Psychotropic Medications
            - # Administrations,
            - Therapeutic Guidances
            """


class patient_entry(models.Model):
    Gender = models.CharField(max_length=20, blank=True, default="")
    Age = models.IntegerField(max_length=20, blank=True, default="")
    Race = models.CharField(max_length=20, blank=True, default="")
    Diagnosis = models.CharField(max_length=256, blank=True, default="")
    MD = models.CharField(max_length=20, blank=True, default="")
    Assignment = models.CharField(max_length=20, blank=True, default="")
    EMR = models.CharField(max_length=20, blank=True, default="")
    LOS = models.IntegerField(max_length=20, blank=True, default="")
    RAR = models.IntegerField(max_length=20, blank=True, default="")
    A = models.IntegerField(max_length=20, blank=True, default="")
    B = models.IntegerField(max_length=20, blank=True, default="")
    C = models.IntegerField(max_length=20, blank=True, default="")
    D = models.IntegerField(max_length=20, blank=True, default="")
    E = models.IntegerField(max_length=20, blank=True, default="")
    F = models.IntegerField(max_length=20, blank=True, default="")
    G = models.IntegerField(max_length=20, blank=True, default="")
    H = models.IntegerField(max_length=20, blank=True, default="")
    I = models.IntegerField(max_length=20, blank=True, default="")
    J = models.IntegerField(max_length=20, blank=True, default="")
    K = models.IntegerField(max_length=20, blank=True, default="")
    L = models.IntegerField(max_length=20, blank=True, default="")
    M = models.IntegerField(max_length=20, blank=True, default="")
    N = models.IntegerField(max_length=20, blank=True, default="")
    O = models.IntegerField(max_length=20, blank=True, default="")
    P = models.IntegerField(max_length=20, blank=True, default="")
    Q = models.IntegerField(max_length=20, blank=True, default="")
    R = models.IntegerField(max_length=20, blank=True, default="")
    S = models.IntegerField(max_length=20, blank=True, default="")
    T = models.IntegerField(max_length=20, blank=True, default="")
    U = models.IntegerField(max_length=20, blank=True, default="")
    V = models.IntegerField(max_length=20, blank=True, default="")
    W = models.IntegerField(max_length=20, blank=True, default="")
    X = models.IntegerField(max_length=20, blank=True, default="")
    Y = models.IntegerField(max_length=20, blank=True, default="")
    Z = models.IntegerField(max_length=20, blank=True, default="")
    AA = models.IntegerField(max_length=20, blank=True, default="")
    AB = models.IntegerField(max_length=20, blank=True, default="")
    AC = models.IntegerField(max_length=20, blank=True, default="")
    AD = models.IntegerField(max_length=20, blank=True, default="")
    PsychotropicMedications = models.IntegerField(max_length=20, blank=True, default="")
    Administrations = models.IntegerField(max_length=20, blank=True, default="")
    TherapeuticGuidances = models.CharField(max_length=20, blank=True, default="")

    class Meta:
        ordering = ["created"]
