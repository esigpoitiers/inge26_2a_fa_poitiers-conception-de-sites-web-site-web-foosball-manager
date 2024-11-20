from models.user import User
from cs50 import SQL


class UserController:
    def __init__(self, db: SQL):
        self.db = db
        
    def get_by_id(self, user_id: int) -> User:
        return User(self.db.execute("SELECT * FROM users WHERE id = ?", user_id))