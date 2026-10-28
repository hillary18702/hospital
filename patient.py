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

    # def change_password():
    #     try:
    #         id=int(input("Enter the patient's id: "))
    #         for patient in patients:
    #             if patient['id']== id:
    #                 old_password=input("Enter the old password: ")
    #                 if patient.get('password') != old_password:
    #                     return "incorrect password"

    #                 new_password=input("Enter the new password: ")
    #                 confirm_password=input("Enter the new password again: ")
    #                 if new_password != confirm_password:
    #                     return "password do not match"
    #                 patient['password']=new_password
    #                 return "password changed successfully!"
    #             return "patient not found"

    #     except ValueError:
    #         return "Enter a valid id"
    
    

    def update_patient():
        try:
            id=int(input("Enter the patient's id: "))
            name=input("Enter the patient's name: ")
            national_id=input("Enter the patient's national id: ")
            county=input("Enter the patient's county: ")
            sub_county=input("Enter the patient's sub county: ")
            location=input("Enter the patient's location: ")
            test=input("Enter the test performed: ")
            result=input("Enter the test results: ")
            impression=input("Enter the patient's impression: ")

            updated_patient= {
                "id": id,
                "name": name,
                "national_id": national_id,
                "address": {"county": county, 'sub-county': sub_county, 'location': location},
                "prescription":{'test': test, 'result': result, 'impression': impression}  
            }
            for index, patient in enumerate(patients):
                if patient['id']==id:
                    patients[index] = updated_patient

            return patients
                    


        except ValueError:
            return "Please enter a valid ID"


    def remove_patient():
        id=int(input("Enter the patient's ID: "))
        for patient in patients:
            if patient['id'] == id:
                patients.pop(patients.index(patient))

        return patients
