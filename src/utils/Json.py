import json


class Json:
    def __init__(self, file):
        self.file = file
        self.encoding = 'utf-8'
        self.data = self.get_json_data()

    # когда нет пользователей...
    def handle_empty_json(self):
        print('json is empty. Writing empty array...')
        empty_array = []

        with open(self.file, 'w', encoding=self.encoding) as users_file:
            json.dump(empty_array, users_file)

        return empty_array

    def is_user_exists(self, userID):
        for user in self.data:
            print('user', user)
            if user['id'] == userID:
                return True
            return False

    # вытягиваем юзеров
    def get_json_data(self):
        with open(self.file, "r", encoding=self.encoding) as users_file:
            try:
                data = json.load(users_file)
                # print('json file data: ', data)
            except Exception as e:
                data = self.handle_empty_json()

            return data

    # регистрируем юзеров
    def saveUser(self, user):
        is_registered = self.is_user_exists(user['id'])
        print('Зареганый в БД?: ', is_registered)

        # если зарегистрирован...
        if is_registered:
            print(
                f"Пользователь @{user['username']} с именем '{user['first_name']}' уже зарегистрирован в боте!")
            return

        self.data.append(user)
        with open(self.file, 'w', encoding=self.encoding) as users_file:
            json.dump(self.data, users_file, ensure_ascii=False)
            print(
                f"Пользователь @{user['username']} с именем '{user['first_name']}' только что зарегистрировался в боте!")
 
    # достаём доступ юзера (role / access)
    def get_user_access(self, id):  # на основе id из JSON
        user_id = id
        users_data = self.get_json_data()
        print('users data: ', users_data)
