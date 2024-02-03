from lib.listing import Listing

class ListingRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self, filter=None):
        if filter:
            rows = self._connection.execute('SELECT * FROM listings WHERE user_id <> %s', [filter])
        else:
            rows = self._connection.execute('SELECT * FROM listings')
        
        list_to_return = []

        for row in rows:
            listing = Listing(row['id'], row['name'], row['descr'], row['price'], row['user_id'])
            list_to_return.append(listing)

        if len(list_to_return):
            return list_to_return

    def find(self, id, filter="id"):
        if filter == "id":
            rows = self._connection.execute("SELECT * FROM listings WHERE id=%s", [id])
            if rows:
                row = rows[0]
                listing = Listing(row['id'], row['name'], row['descr'], row['price'], row['user_id'])
                return listing
            else:
                return "Error fetching data"
        elif filter == "user_id":
            rows = self._connection.execute("SELECT * FROM listings WHERE user_id=%s", [id])
            if rows:
                listings = []
                for row in rows:
                    listing = Listing(row['id'], row['name'], row['descr'], row['price'], row['user_id'])
                    listings.append(listing)
                return listings
            else:
                return "Error fetching data"
        else:
            return "Generic Error"
        
    
    def add(self, listing):
        self._connection.execute("INSERT INTO listings (name, descr, price, user_id) VALUES (%s, %s, %s, %s)", [listing.name, listing.desc, listing.price, listing.user_id])
    
    def update(self, listing):
        self._connection.execute("UPDATE listings SET name=%s, descr=%s, price=%s WHERE id=%s", [listing.name, listing.desc, listing.price, listing.id])
    
    def delete(self, id):
        self._connection.execute("DELETE FROM listings WHERE id=%s", [id])
    
    def get_id(self):
        row = self._connection.execute("SELECT lastval()")
        return row[0]['lastval']