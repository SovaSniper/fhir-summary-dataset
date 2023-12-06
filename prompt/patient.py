import json
from fhir.resources.patient import Patient

def prompt(resource):
    prompted = ""
    try:
        fhirResource = Patient.parse_raw(json.dumps(resource))

        data = [
            fhirResource.id,
            fhirResource.active,
            fhirResource.name[0].family,
            fhirResource.name[0].given[0],
            fhirResource.gender,
            fhirResource.birthDate,
            fhirResource.address[0].line[0],
            fhirResource.address[0].city,
            fhirResource.address[0].state,
            fhirResource.address[0].postalCode,
        ]
        data = [i for i in data if i is not None]

        prompted += "Patient "
        for info in data:
            if info is None:
                continue
            prompted += str(info) + " "

    except Exception as e:
        print(e)

    return " ".join(prompted.split())

