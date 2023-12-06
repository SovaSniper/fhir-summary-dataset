import json
from fhir.resources.diagnosticreport import DiagnosticReport

def prompt(resource):
    prompted = ""
    try:
        if "context" in resource:
            del resource["context"]
        
        fhirResource = DiagnosticReport.parse_raw(json.dumps(resource))

        data = [
            # fhirResource.id,
            fhirResource.code.coding[0].display,
            fhirResource.effectiveDateTime,
            # fhirResource.subject.reference,
        ]
        data = [i for i in data if i is not None]

        prompted += "Diagnosis Report "
        for info in data:
            if info is None:
                continue
            prompted += str(info) + " "

    except Exception as e:
        print(e)

    return " ".join(prompted.split())
