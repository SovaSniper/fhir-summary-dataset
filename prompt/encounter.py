import json
from fhir.resources.encounter import Encounter


def prompt(resource):
    print("Encounter")
    prompted = ""
    try:
        if "period" in resource:
            del resource["period"]
        if "class" in resource:
            del resource["class"]
        if "reason" in resource:
            converted_reason = {
                "reason": [
                    {
                        "value": [
                            {
                                "concept": {
                                    "text": resource["reason"][0]["coding"][0]["display"]
                                }
                            }
                        ]
                    }
                ]
            }
            resource["reason"] = converted_reason["reason"]
        fhirResource = Encounter.parse_raw(json.dumps(resource))

        data = [
            # fhirResource.id,
            fhirResource.type[0].text,
            fhirResource.plannedStartDate.start,
            # fhirResource.effectivePeriod.end,
        ]
        if fhirResource.reason is not None:
            # resource["reason"][0]["coding"][0]["display"]
            # data.append(fhirResource.reason[0]["coding"][0].display)
            data.append(resource["reason"][0]["coding"][0]["display"])
        data = [i for i in data if i is not None]

        prompted += "Encounter "
        for info in data:
            if info is None:
                continue
            prompted += str(info) + " "

    except Exception as e:
        print(e)

    return " ".join(prompted.split())
