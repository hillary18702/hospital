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
                resp['status']=400
                return resp

            else:
                resp['message']="Username or Password incorrect!"
                resp['status'] = 401
                return resp

        # return resp
