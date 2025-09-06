class Stadium:
    def __init__(self, stadium_name="", date_of_opening="", country="", city="", seating_capacity=0):
        self.stadium_name = stadium_name
        self.date_of_opening = date_of_opening
        self.country = country
        self.city = city
        self.seating_capacity = seating_capacity

    def fill_data(self):
        self.stadium_name = input("Stadium name: ")
        self.date_of_opening = input("Date of opening: ")
        self.country = input("Country: ")
        self.city = input("City: ")
        self.seating_capacity = int(input("Seating capacity: "))

    def get_stadium_name(self):
        print(f"Stadium name: {self.stadium_name}")
    def get_date_of_opening(self):
        print(f"Date of opening: {self.date_of_opening}")
    def get_country(self):
        print(f"Country: {self.country}")
    def get_city(self):
        print(f"City: {self.city}")
    def get_seating_capacity(self):
        print(f"Seating capacity: {self.seating_capacity}")


storage = Stadium()

while True:
    print()
    guess_1 = input("fill/output: ")
    if guess_1 == "fill":
        storage.fill_data()
    elif guess_1 == "output":
        guess = input("Select (Stadium/Date/Country/City/Capacity): ")
        if guess == "Stadium":
            storage.get_stadium_name()
        elif guess == "Date":
            storage.get_date_of_opening()
        elif guess == "Country":
            storage.get_country()
        elif guess == "City":
            storage.get_city()
        elif guess == "Capacity":
            storage.get_seating_capacity()
    else:
        print("again try")
