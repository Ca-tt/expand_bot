import os
from dotenv import load_dotenv

load_dotenv()


class Dotenv():
    def __init__(self):
        load_dotenv()
        
        self.bot_token = ''
        self.admin_id = ''
        self.student_ids = ''
        
        self.get_env_data()
        
    def get_env_data(self):
        self.bot_token = os.getenv('BOT_TOKEN')
        self.admin_id = int(os.getenv('ADMIN_ID'))
        self.student_ids = [int(item) for item in os.getenv('STUDENT_IDS').split(',')]
        

