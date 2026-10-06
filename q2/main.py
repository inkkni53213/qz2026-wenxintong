import json
import os

class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1
