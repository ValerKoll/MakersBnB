class Listing():
    def __init__(self, id, name, desc, price, user_id=None):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.user_id = user_id
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, desc: {self.desc}, price: {self.price}"