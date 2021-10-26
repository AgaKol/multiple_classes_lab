class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers = []

    def pick_up_from_stop(self, stop):
        for person in stop.queue:
            self.pick_up(stop.queue)
        stop.queue.clear()
