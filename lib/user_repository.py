from lib.user import User

class UserRepository():    
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        list_to_return = []
        for row in rows:
            entry = User(row["id"], row["fullname"], row["email_address"], row["passcode"])
            list_to_return.append(entry)
        if len(list_to_return):
            return list_to_return
    
    def find(self, email_address, password):
        rows = self._connection.execute(
            "SELECT * FROM users WHERE (email_address = %s AND passcode = %s)", [email_address, password]
            )
        # future TODOs: Implement error checks collector
        if rows:
            row = rows[0]
            user = User(row['id'], row['fullname'], row['email_address'], row['passcode'])
            if user.is_valid():
                return (True, user)
            return (False, 'Stored values not valid')
        return (False, "User not found")
    
    def add(self, id, fullname, email_address, password):
        user = User(id, fullname, email_address, password)
        if user.is_valid():
            self._connection.execute(
                'INSERT INTO users (fullname, email_address, passcode) VALUES (%s, %s, %s)', [user.fullname, user.email_address, user.password]
                )
            row = self._connection.execute(
                "SELECT id FROM users WHERE (email_address = %s AND passcode = %s)", [user.email_address, user.password]
                )
            user.id = id
            return (True, user)
        return (False, user.errors)
    
    #to be implemented
    def update(self, user):
        pass
    #to be implemented
    def delete(self, user_id):
        pass