from rest_framework import serializers
from .models import patient_entry


class patient_entriesSerializer(serializers.ModelSerializer):
    class Meta:

        model = patient_entry
        fields = [
            "id",
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
