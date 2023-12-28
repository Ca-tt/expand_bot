import os
from dotenv import load_dotenv

load_dotenv()


class Dotenv():
    def __init__(self, config_name: str):
        self.config_name = config_name

    # loads configs from .env
    def load_env_data(self):
        # load dotenv information
        print(f"loading {self.config_name}...")

        # getting info...
        loaded_info = os.getenv(self.config_name)

        # trasform data
        loaded_info = self.transform_data(loaded_info)
        # just for printing dividers
        print(f"loaded {self.config_name} successfully")
        print(f"{'='*10}\n")

        return loaded_info
        # end

    def transform_data(self, data):
        if self.config_name == 'ADMIN_ID':
            data = int(data)

        elif self.config_name == 'STUDENTS_IDS':
            data = data.split(',')
            
            for i in range(len(data)):
                data[i] = int(data[i])

        return data
