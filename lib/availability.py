class Availability:
    def __init__(self, date_from, date_to, space_id, id=None):
        self.id = id
        self.date_from = date_from
        self.date_to = date_to
        self.space_id = space_id