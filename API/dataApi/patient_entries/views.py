from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import patient_entry, patient_entry_test
from .serializers import patient_entriesSerializer, patient_entries_testSerializer


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

class patient_entry_testViewSet(viewsets.ModelViewSet):
    model = patient_entry_test
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
    queryset = patient_entry_test.objects.all()
    serializer_class = patient_entries_testSerializer