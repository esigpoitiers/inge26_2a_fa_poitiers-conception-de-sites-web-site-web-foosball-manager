from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, login, password):
        self.login = login
        self.password_hash = generate_password_hash(password)
        # ...

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_session(self):
        """Export user data for session storage"""
        return {
            "id": self.id,
            "login": self.login,
            # ...
        }
