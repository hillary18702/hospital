from auth import Auth
from patient import Patient

IS_LOGIN=False

def entry_action():
    global IS_LOGIN
    username=input("Enter username: ")
    password = input("Enter password: ")

    

    login= Auth.login(username, password)
    print(login)

    if login['status'] == 400:
        print("Logged in")
        # print(login)
        IS_LOGIN=True

        while IS_LOGIN:
            act=action()
            operation= activity(act)
            print(operation)

    else:
        print(login)
        print(login["message"])


def action():
    print("Welcome to Oswago Hospital!")
    print("Please select the activity that you want to perform")
    print("1. Create patient")
    print("2. Update patient details")
    print("3. Get a patient")
    print("4. Get all patients")
    print("5. Remove patient")
    print("6. Logout")
    choice=input("Enter the activity: ")
    return choice


def activity(choice):
    global IS_LOGIN
    try:
        if int(choice) == 1:
            response= Patient.create_patient()
            print(response)

        elif int(choice) == 2:
            pass
        elif int(choice) == 3:
            response= Patient.get_patient()
            print(response)

        elif int(choice) == 4:
            response=Patient.get_all_patient()
            print(response)

        elif int(choice) == 5:
            response = Patient.remove_patient()
            print(response)

        elif int(choice) == 6:
            IS_LOGIN=False
            

    except ValueError:
        return "Please provide a valid choice"


entry_action()