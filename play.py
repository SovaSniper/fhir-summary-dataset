import re
import json
from fhir.resources.medication import Medication
from prompt.medication import prompt as promptMedication
from prompt.immunization import prompt as promptImmunization
from prompt.observation import prompt as promptObservation
from prompt.condition import prompt as promptCondition
from prompt.encounter import prompt as promptEncounter
from prompt.diagnosticreport import prompt as promptDiagnosticReport
from prompt.patient import prompt as promptPatient

def prompt(data):
    information = []
    ret = "Generate a concise and informative clinical summary paragraph for "
    for resource in data["entry"]:
        input = ""
        if resource["resource"]["resourceType"] == "Patient":
            ret += f"{promptPatient(resource['resource'])}"
            # input = promptPatient(resource["resource"])
        if resource["resource"]["resourceType"] == "Medication":
            input = promptMedication(resource["resource"])
        elif resource["resource"]["resourceType"] == "Immunization":
            input = promptImmunization(resource["resource"])
        elif resource["resource"]["resourceType"] == "Observation":
            input = promptObservation(resource["resource"])
        elif resource["resource"]["resourceType"] == "Condition":
            input = promptCondition(resource["resource"])
        elif resource["resource"]["resourceType"] == "DiagnosticReport":
            input = promptDiagnosticReport(resource["resource"])
        # elif resource["resource"]["resourceType"] == "Encounter":
        #     input = promptEncounter(resource["resource"])
        # else:
        #     print(resource["resource"]["resourceType"])

        information.append(input)

    information = [i for i in information if i != '']

    # ret = f"Generate an informative overview paragraph that summarizes the patient's medical history, treatment course, and the current situation: Compose a comprehensive overview paragraph for {' '.join(information)}"
    # ret = f"Generate a comprehensive overview paragraph that summarizes the patient's medical history, treatment course, and includes relevant clinical information: Generate an informative overview paragraph for patient {' '.join(information)}"
    ret += f". Summarize in a one A4 page length report patient's medical history, treatment course, and include relevant clinical information, advice, and a clear course of action. Ensure the summary is comprehensive yet concise to assist doctors in effectively engaging with the patient and guiding their ongoing care based on the provided data, including vital signs, immunizations, and diagnosis reports with the given data: {' '.join(information)}"

    return ret

# Load json data
data = json.load(open("./dataset/1/Darrin898_Botsford977_7d22f1a2-2936-df06-38b1-6c2d216b1907.json"))
prom = prompt(data)

with open("prompt.txt", 'w') as file:
    file.write(prom)
