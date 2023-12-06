import json
from fhir.resources.immunization import Immunization

def prompt(resource):
    prompted = ""
    try:
        if "occurrenceDateTime" not in resource:
            resource["occurrenceDateTime"] = resource["date"]
            del resource["date"]
            del resource["notGiven"]
        fhirResource = Immunization.parse_raw(json.dumps(resource))

        data = [
            # fhirResource.id,
            fhirResource.status,
            fhirResource.vaccineCode.coding[0].display,
            # fhirResource.patient.reference,
            fhirResource.occurrenceDateTime.isoformat(),
        ]
        data = [i for i in data if i is not None]

        prompted += "Immunization "
        for info in data:
            if info is None:
                continue
            prompted += str(info) + " "

    except Exception as e:
        print(e)

    return " ".join(prompted.split())
