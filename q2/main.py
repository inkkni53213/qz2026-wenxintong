import json
import os

class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, name, age):
        user = {
            "id": self.next_id,
            "name": name,
            "age": age
        }
        self.users.append(user)
        self.next_id += 1  
        return user

    def get_user(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def update_age(self, user_id, new_age):
        user = self.get_user(user_id)
        if user is not None:
            user["age"] = new_age
            return True
        return False

    def remove_user(self, user_id):
        user = self.get_user(user_id)
        if user is not None:
            self.users.remove(user)
            return True
        return False

    def list_users(self):
        return self.users

    def save_to_json(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.users, f, ensure_ascii=False, indent=4)

    def load_from_json(self, filepath):
        if not os.path.exists(filepath):
            return

        with open(filepath, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
            self.users = loaded_data

        if self.users:
            max_id = max(user["id"] for user in self.users)
            self.next_id = max_id + 1
        else:
            self.next_id = 1
