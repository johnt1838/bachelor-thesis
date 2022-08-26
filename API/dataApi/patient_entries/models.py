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
    Age = models.IntegerField()
    Race = models.CharField(max_length=20, blank=True, default="")
    Diagnosis = models.CharField(max_length=256, blank=True, default="")
    MD = models.CharField(max_length=20, blank=True, default="")
    Assignment = models.CharField(max_length=20, blank=True, default="")
    EMR = models.CharField(max_length=20, blank=True, default="")
    LOS = models.IntegerField()
    RAR = models.IntegerField()
    A = models.IntegerField()
    B = models.IntegerField()
    C = models.IntegerField()
    D = models.IntegerField()
    E = models.IntegerField()
    F = models.IntegerField()
    G = models.IntegerField()
    H = models.IntegerField()
    I = models.IntegerField()
    J = models.IntegerField()
    K = models.IntegerField()
    L = models.IntegerField()
    M = models.IntegerField()
    N = models.IntegerField()
    O = models.IntegerField()
    P = models.IntegerField()
    Q = models.IntegerField()
    R = models.IntegerField()
    S = models.IntegerField()
    T = models.IntegerField()
    U = models.IntegerField()
    V = models.IntegerField()
    W = models.IntegerField()
    X = models.IntegerField()
    Y = models.IntegerField()
    Z = models.IntegerField()
    AA = models.IntegerField()
    AB = models.IntegerField()
    AC = models.IntegerField()
    AD = models.IntegerField()
    PsychotropicMedications = models.IntegerField()
    Administrations = models.IntegerField()
    TherapeuticGuidances = models.CharField(max_length=20, blank=True, default="")

class patient_entry_test(models.Model):
    Gender = models.CharField(max_length=20, blank=True, default="")
    Age = models.IntegerField()
    Race = models.CharField(max_length=20, blank=True, default="")
    Diagnosis = models.CharField(max_length=256, blank=True, default="")
    MD = models.CharField(max_length=20, blank=True, default="")
    Assignment = models.CharField(max_length=20, blank=True, default="")
    EMR = models.CharField(max_length=20, blank=True, default="")
    LOS = models.IntegerField()
    RAR = models.IntegerField()
    A = models.IntegerField()
    B = models.IntegerField()
    C = models.IntegerField()
    D = models.IntegerField()
    E = models.IntegerField()
    F = models.IntegerField()
    G = models.IntegerField()
    H = models.IntegerField()
    I = models.IntegerField()
    J = models.IntegerField()
    K = models.IntegerField()
    L = models.IntegerField()
    M = models.IntegerField()
    N = models.IntegerField()
    O = models.IntegerField()
    P = models.IntegerField()
    Q = models.IntegerField()
    R = models.IntegerField()
    S = models.IntegerField()
    T = models.IntegerField()
    U = models.IntegerField()
    V = models.IntegerField()
    W = models.IntegerField()
    X = models.IntegerField()
    Y = models.IntegerField()
    Z = models.IntegerField()
    AA = models.IntegerField()
    AB = models.IntegerField()
    AC = models.IntegerField()
    AD = models.IntegerField()
    PsychotropicMedications = models.IntegerField()
    Administrations = models.IntegerField()
    TherapeuticGuidances = models.CharField(max_length=20, blank=True, default="")