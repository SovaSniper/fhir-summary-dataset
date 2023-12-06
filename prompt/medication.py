import json
from fhir.resources.medication import Medication

data = {
    "fullUrl": "urn:uuid:bfa957bb-95d6-42b9-9d62-8ee3700e8683",
    "resource": {
        "id": "bfa957bb-95d6-42b9-9d62-8ee3700e8683",
        "meta": {
            "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-medication-Medication"
            ],
            "tag": [
                {"system": "https://smarthealthit.org/tags", "code": "synthea-7-2017"}
            ],
        },
        "code": {
            "coding": [
                {
                    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                    "code": "834101",
                    "display": "Penicillin V Potassium 500 MG",
                }
            ],
            "text": "Penicillin V Potassium 500 MG",
        },
        "resourceType": "Medication",
    },
}


def prompt(resource):
    prompted = ""
    try:
        fhirResource = Medication.parse_raw(json.dumps(resource))

        data = [
            # fhirResource.id,
            fhirResource.code.coding[0].code,
            fhirResource.code.text,
            fhirResource.status,
        ]
        data = [i for i in data if i is not None]

        prompted += "Medication "
        for info in data:
            if info is None:
                continue
            prompted += str(info) + " "

    except Exception as e:
        print(e)

    return " ".join(prompted.split())
