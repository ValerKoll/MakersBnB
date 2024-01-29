from lib.availability import Availability

class AvailabilityRepository():
    def __init__(self, connection):
        self._connection = connection

    def add(self, availability:Availability):
        self._connection.execute("INSERT INTO availabilities (date_from, date_to, space_id) VALUES (%s, %s, %s)", [availability.date_from, availability.date_to, availability.space_id])
    
    def find(self, space_id):
        rows = self._connection.execute("SELECT * FROM availabilities WHERE space_id=%s", [space_id])
        availabilities = []

        for row in rows:
            availability = Availability(row['date_from'], row['date_to'], row['space_id'])
            availabilities.append(availability)

        return availabilities