from datetime import datetime

# helpers
from utils.Json import Json
from utils.Dotenv import Dotenv


# JSON handling
USERS_FILE = "json/users.json"
json_users = Json(file=USERS_FILE)

# chosen users list
admin_id = Dotenv().admin_id
students_ids = Dotenv().student_ids


class User:
    def __init__(self, message):
        self.first_name = message.chat.first_name.encode().decode('utf-8')
        self.username = message.chat.username
        self.id = message.chat.id
        self.signup_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.access = self.setAccessLevel()

        # save user to json
        self.saveUserToJson()

    # define access level
    def setAccessLevel(self):
        access = 'partner'

        if self.id in students_ids:
            access = 'student'

        elif self.id == admin_id:
            access = 'admin'

        return access

    # save user to json
    def saveUserToJson(self):
        new_user = {
            "first_name": self.first_name,
            "username": self.username,
            "id": self.id,
            "access": self.access,
            "registration_date": self.signup_date,
        }
        print("🐍 File: users/User.py | Line: 49 | saveUserToJson ~ new_user",new_user)
        

        json_users.saveUser(new_user)

    # def saveAction(self):
        # print('test: ')


""" 
    User actions:
    - registration 
    - command used 
    - leave chat (idle for 10s-15s) 
    - filled in some data
    - press a button
    - choose a menu link / (or go to specific menu option)

    Structure: 
    [
        "Дамир": [
            {
                "time": "18:09:23 28-12-2023",
                "comment": "зашёл в бота", 
                "action_type": "login", 
                "command": "/start", 
            },
            {
                "time": "18:10:01 28-12-2023",
                "comment": "нажал /start", 
                "action_type": "login", 
                "command": "/start", 
            },
            {
                "time": "18:11:20 28-12-2023",
                "comment": "вышел из бота", 
                "action_type": "logout", 
                "command": "", 
            },
        ]
    ]
"""
