class vehicle:
    def __init__(self,fare,seats):
        self.fare = fare
        self.seats = seats
    
class bus(vehicle):
    def __init__(self, fare, seats):
        super().__init__(fare,seats)
        def calculate_total_fare(self,passengers):
            if passengers > self.seats:
                return "seats not available"
            else:
                return self.fare * passengers

people = int(input("enter the number of people:"))

bus_fare = bus(50, 40)
total_fare = bus_fare.calculate_total_fare(people)
print("Total fare for", people, "people is:", total_fare)
