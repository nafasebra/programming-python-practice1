class Flight:
    def __init__(self, flight_type, flight_time, origin, destination):
        self.flight_type = flight_type
        self.flight_time = flight_time
        self.origin = origin
        self.destination = destination
        self.seats = []
        for i in range(40):
          self.seats.append(0)

    def findFirstClassSeat(self):
        for i in range(20):
            if self.seats[i] is 0:
                return i
            return -1

    def findEconomySeat(self):
        for i in range(20, 40):
            if self.seats[i] is 0:
                return i
        return -1

    def reserveFirstClassSeat(self, card):
        for i in range(20):
            if self.seats[i] is 0:
                self.seats[i] = card
                break

    def reserveEconomySeat(self, card):
        for i in range(20, 40):
            if self.seats[i] is 0:
                self.seats[i] = card
                break


class FlightCard:
    def __init__(self, firstname, lastname, flight_type, origin, destination, flight_time, seat_type):
        self.firstname = firstname
        self.lastname = lastname
        self.flight_type = flight_type
        self.origin = origin
        self.destination = destination
        self.flight_time = flight_time
        self.seat_type = seat_type


class AirlineReservationSystem:
    def __init__(self):
        self.flights = []
        self.flight_cards = []
        self.seat_availability = [0] * 41

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_flight_card(self, flight_card):
        self.flight_cards.append(flight_card)

    def reserveFirstClassSeat(self, card):
        for flight in self.flights:
            if flight.flight_type == card.flight_type and flight.flight_time == card.flight_time:
                if flight.findFirstClassSeat() != -1:
                    flight.reserveFirstClassSeat(card)
                    return True
        return False

    def reserveEconomySeat(self, card):
        for flight in self.flights:
            if flight.flight_type == card.flight_type and flight.flight_time == card.flight_time:
                if flight.findEconomySeat() != -1:
                    flight.reserveEconomySeat(card)
                    return True
        return False

    def reserve_seat(self, card):
        if card.seat_type == 1:
            if self.reserveFirstClassSeat(card):
                return True
            else:
                print("No first class seat found")
                answer = input("Would you like to reserve an economy seat? (y/n)\n")
                if answer == "y":
                    if self.reserveEconomySeat(card):
                        return True
                    else:
                        print("No economy seat found")
                        return False

        else:
            if self.reserveEconomySeat(card):
                return True
            else:
                print("No economy seat found")
                return False

    def find_nearest_flight(self, card):
        nearest_flights = []

        for flight in self.flights:
            if flight.flight_type == card.flight_type and flight.origin == card.origin and flight.destination == card.destination and abs(
                    flight.flight_time - card.flight_time) != 0:
                nearest_flights.append(flight)

        nearest_flights.sort(key=lambda x: abs(card.flight_time - x.flight_time))

        if nearest_flights:
            return nearest_flights[0]

        return 0

    def reverse_seat_nearest_flight(self, card):
        nearest_flight = self.find_nearest_flight(card)

        if nearest_flight is 0:
            return False

        if card.seat_type == 1:
            if nearest_flight.findFirstClassSeat() != -1:
                nearest_flight.reserveFirstClassSeat(card)
                return True
            else:
                print("No first class seat found")
                answer = input("Would you like to reserve an economy seat? (y/n)\n")
                if answer == "y":
                    if nearest_flight.findEconomySeat() != -1:
                        nearest_flight.reserveEconomySeat(card)
                        return True
                    else:
                        print("No economy seat found")
                        return False

        else:
            if nearest_flight.findEconomySeat() != -1:
                nearest_flight.reserveEconomySeat(card)
                return True
            else:
                print("No economy seat found")
                return False

    def display_flights(self):
        if not self.flights:
            print('The flight list is empty.')
            return

        for i, flight in enumerate(self.flights):
            print(f"Flight {i + 1}")
            print(f"Flight Type: {flight.flight_type}")
            print(f"Flight Time: {flight.flight_time}")
            print(f"Origin: {flight.origin}")
            print(f"Destination: {flight.destination}")
            print()

    def display_flight_cards(self):
        if not self.flight_cards:
            print('The flight cards list is empty.')
            return

        for i, card in enumerate(self.flight_cards):
            print(f"Flight Card {i + 1}")
            print(f"First Name: {card.firstname}")
            print(f"Last Name: {card.lastname}")
            print(f"Flight Type: {card.flight_type}")
            print(f"Flight Time: {card.flight_time}")
            print(f"Origin: {card.origin}")
            print(f"Destination: {card.destination}")
            print(f"Seat Type: {'First Class' if card.seat_type == 1 else 'Economy'}")
            print()


def main():
    system = AirlineReservationSystem()

    while True:
        print()
        print("==== Airline Reservation System ====")
        print("1. Add Flight")
        print("2. Add Flight Card")
        print("3. Display Flights")
        print("4. Display Flight Cards")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print()
        match choice:
          case "1":
              flight_type = input("Enter flight type (Domestic/Foreign): ")
              if flight_type not in ["Domestic", "Foreign"]:
                  print("Invalid flight type!")
                  continue
              flight_time = int(input("Enter flight time: "))
              if flight_time < 1 or flight_time > 24:
                  print("Invalid flight time!")
                  continue
              origin = input("Enter origin: ")
              destination = input("Enter destination: ")
              flight = Flight(flight_type, flight_time, origin, destination)
              system.add_flight(flight)
              print("The flight added to the flights list successfully")
          case "2":
              firstname = input("Enter first name: ")
              lastname = input("Enter last name: ")
              flight_type = input("Enter flight type (Domestic/Foreign): ")
              if flight_type not in ["Domestic", "Foreign"]:
                  print("Invalid flight type!")
                  continue
              origin = input("Enter origin: ")
              destination = input("Enter destination: ")
              flight_time = int(input("Enter flight time: "))
              if flight_time < 1 or flight_time > 24:
                  print("Invalid flight time!")
                  continue
              seat_type = int(input("Enter seat type (1 for First Class, 2 for Economy): "))
              if seat_type not in [1, 2]:
                  print("Invalid seat type!")
                  continue
              flight_card = FlightCard(firstname, lastname, flight_type, origin, destination, flight_time, seat_type)
              if system.reserve_seat(flight_card):
                  system.add_flight_card(flight_card)
                  print("The flight card added to the flight cards list successfully")
              else:
                  answer = input("Would you like to reserve a seat for you on the nearest flight? (y/n)\n")
                  if answer == "y":
                      if system.reverse_seat_nearest_flight(flight_card):
                          system.add_flight_card(flight_card)
                          print("The flight card added to the flight cards list successfully")
          case "3":
              system.display_flights()
          case "4":
              system.display_flight_cards()
          case "5":
              break
          case _:
              print("Invalid choice!, Please try again :)")

# run main function
main()
