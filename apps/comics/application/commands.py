class RentComicCommand:

    def __init__(self, id, days, client, rented_at, comicId):
        self.id = id
        self.days = days
        self.client = client
        self.rented_at = rented_at
        self.comicId = comicId
