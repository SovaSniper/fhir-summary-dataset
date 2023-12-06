import json
from fhir.resources.observation import Observation

def prompt(resource):
    prompted = ""
    try:
        if "context" in resource:
            del resource["context"]
        fhirResource = Observation.parse_raw(json.dumps(resource))

        data = [
            # fhirResource.id,
            fhirResource.status,
            fhirResource.code.coding[0].display,
            # fhirResource.subject.reference,
        ]
        if not fhirResource.valueQuantity == None:
            data.extend(
                [fhirResource.valueQuantity.value, fhirResource.valueQuantity.unit]
            )
        if not fhirResource.component == None:
            for component in fhirResource.component:
                data.extend(
                    [component.valueQuantity.value, component.valueQuantity.unit]
                )
        data = [i for i in data if i is not None]

        prompted += "Observation "
        for info in data:
            if info is None:
                continue
            prompted += str(info) + " "

    except Exception as e:
        print(e)

    return " ".join(prompted.split())


# data = {}
# print(prompt(data["resource"]))
