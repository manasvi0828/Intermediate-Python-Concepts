class Vehicles:
    def __init__(self):
        self.seating_capacity= 50


class Bus(Vehicles):
    def fare_charge(self):
        return self.seating_capacity * 100 + 10/100 * self.seating_capacity *100


bus1= Bus()
print(bus1.fare_charge())