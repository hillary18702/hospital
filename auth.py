import jwt
from users import users
from dotenv import load_dotenv
import os

load_dotenv()
SECRET=os.getenv("SECRET_KEY")

class Auth:


    def login(username, password):
        resp={}
        for user in users:
            if username== user['username'] and password == user["password"]:
                payload={
                    "id": user['id'],
                    "username": user['username'],
                    "role": user['role']
                }
                token= jwt.encode(payload, SECRET, algorithm="HS256")
                resp['message'] = "Login successful"
                resp['token']=token
                resp['role']=user['role']
                resp['status']=201
                return resp

            else:
                resp['message']="Username or Password incorrect!"
                resp['status'] = 401
                return resp

    # return resp
    def change_password():
        try:
            id=int(input("Enter the user's id: "))
            for user in users:
                if user['id']== id:
                    old_password=input("Enter the old password: ")
                    if user.get('password') != old_password:
                        return "incorrect password"

                    new_password=input("Enter the new password: ")
                    confirm_password=input("Enter the new password again: ")
                    if new_password != confirm_password:
                        return "password do not match"
                    user['password']=new_password
                    return "password changed successfully!"
                return "user not found"

        except ValueError:
            return "Enter a valid id"

