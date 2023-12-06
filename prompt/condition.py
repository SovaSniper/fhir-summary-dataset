import json
from fhir.resources.condition import Condition

def prompt(resource):
    prompted = ""
    try:
        if "context" in resource:
            del resource["context"]
        if "assertedDate" in resource:
            del resource["assertedDate"]
        if "clinicalStatus" in resource:
            if type(resource["clinicalStatus"]) is str:
                resource["clinicalStatus"] = {"coding": [{"display": resource["clinicalStatus"]}]}
        if "verificationStatus" in resource:
            del resource["verificationStatus"]
        
        fhirResource = Condition.parse_raw(json.dumps(resource))

        data = [
            # fhirResource.id,
            fhirResource.clinicalStatus.coding[0].display,
            fhirResource.code.coding[0].display,
            # fhirResource.subject.reference,
        ]
        data = [i for i in data if i is not None]

        prompted += "Condition "
        for info in data:
            if info is None:
                continue
            prompted += str(info) + " "

    except Exception as e:
        print(e)

    return " ".join(prompted.split())
