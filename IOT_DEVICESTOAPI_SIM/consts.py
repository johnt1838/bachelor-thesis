"""Hard coded CONSTANTS """


URL_RAW = 'http://127.0.0.1:8000/data/patient_entries/'
URL_RAW_JSON = 'http://127.0.0.1:8000/data/patient_entries/?format=json'
URL_RAW_DATA_TEST = 'http://127.0.0.1:8000/data/patient_entries_test/'

COLUMNS_RAW_DATASET = ['GENDER', 'AGE', 'RACE_ETHNICITY', 'Diagnosis', 'MD', 'Assignment',
                       'EMR', 'LOS', 'RAR', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'PsychotropicMedications',
                       'Administrations', 'TherapeuticGuidances']
HEADERS_POST = {'Content-type': 'application/json', 'Accept': 'application/json'}

# JSON_RAW_DATA = {
#     "Gender": "",
#     "Age": null,
#     "Race": "",
#     "Diagnosis": "",
#     "MD": "",
#     "Assignment": "",
#     "EMR": "",
#     "LOS": null,
#     "RAR": null,
#     "A": null,
#     "B": null,
#     "C": null,
#     "D": null,
#     "E": null,
#     "F": null,
#     "G": null,
#     "H": null,
#     "I": null,
#     "J": null,
#     "K": null,
#     "L": null,
#     "M": null,
#     "N": null,
#     "O": null,
#     "P": null,
#     "Q": null,
#     "R": null,
#     "S": null,
#     "T": null,
#     "U": null,
#     "V": null,
#     "W": null,
#     "X": null,
#     "Y": null,
#     "Z": null,
#     "AA": null,
#     "AB": null,
#     "AC": null,
#     "AD": null,
#     "PsychotropicMedications": null,
#     "Administrations": null,
#     "TherapeuticGuidances": ""
# }