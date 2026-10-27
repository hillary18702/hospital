from wagonjwa import patients

class Patient:

    def create_patient(name=None, national_id=None, address={}, presc={}):
        print("")
        name=input("Enter the patient name: ")
        national_id=input("Enter the patient's national ID number: ")
        county=input("Enter the patient's county: ")
        sub_county=input("Enter the patient's sub-county: ")
        location=input("Enter the patient's location: ")
        address={
            "county": county,
            "sub-county": sub_county,
            "location": location
        }
        patient={
            "id": patients[-1]['id']+1,
            "name": name,
            "national_id": national_id,
            "address": address,
            "prescription":presc
        }
        patients.append(patient)
        return patients

    def get_patient():
        id=int(input("Enter the patient's ID: "))
        for patient in patients:
            if id == patient['id']:
                return patient

    def get_all_patient():
        return patients


    def remove_patient():
        id=int(input("Enter the patient's ID: "))
        for patient in patients:
            if patient['id'] == id:
                print(patient)
                print(patients.index(patient))
                patients.pop(patients.index(patient))

        return patients
