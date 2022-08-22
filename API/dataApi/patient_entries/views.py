from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import patient_entry
from .serializers import patient_entriesSerializer


# Create your views here.
class patient_entryViewSet(viewsets.ModelViewSet):
    model = patient_entry
    fields = [
        "Gender",
        "Age",
        "Race",
        "Diagnosis",
        "MD",
        "Assignment",
        "EMR",
        "LOS",
        "RAR",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "AA",
        "AB",
        "AC",
        "AD",
        "PsychotropicMedications",
        "Administrations",
        "TherapeuticGuidances",
    ]
    queryset = patient_entry.objects.all()
    serializer_class = patient_entriesSerializer
