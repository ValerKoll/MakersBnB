from listing import Listing

class ListingRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self, filter=None):
        if filter:
            rows = self._connection.execute('SELECT * FROM spaces WHERE user_id <> %s', [filter])
        else:
            rows = self._connection.execute('SELECT * FROM spaces')
        
        list_to_return = []

        for row in rows:
            space = Space(row['id'], row['name'], row['descr'], row['price'], row['user_id'])
            list_to_return.append(space)

        if len(list_to_return):
            return list_to_return

    def find(self, id, filter="id"):
        if filter == "id":
            rows = self._connection.execute("SELECT * FROM spaces WHERE id=%s", [id])
            if rows:
                row = rows[0]
                space = Space(row['id'], row['name'], row['descr'], row['price'], row['user_id'])
                return space
            else:
                return "Error fetching data"
        elif filter == "user_id":
            rows = self._connection.execute("SELECT * FROM spaces WHERE user_id=%s", [id])
            if rows:
                spaces = []
                for row in rows:
                    space = Space(row['id'], row['name'], row['descr'], row['price'], row['user_id'])
                    spaces.append(space)
                return spaces
            else:
                return "Error fetching data"
        else:
            return "Generic Error"
        
    
    def add(self, space:Space):
        self._connection.execute("INSERT INTO spaces (name, descr, price, user_id) VALUES (%s, %s, %s, %s)", [space.name, space.desc, space.price, space.user_id])
    
    def update(self, space:Space):
        self._connection.execute("UPDATE spaces SET name=%s, descr=%s, price=%s WHERE id=%s", [space.name, space.desc, space.price, space.id])
    
    def delete(self, id):
        self._connection.execute("DELETE FROM spaces WHERE id=%s", [id])
    
    def get_id(self):
        row = self._connection.execute("SELECT lastval()")
        return row[0]['lastval']