flights = [
    {"flight_num": "001", "origin": "USA", "destination": "Canada", "departure_time": "10:00 AM", "flight_type": "One Way", "seats": {"First Class": list(range(1, 21)), "Economy": list(range(21, 41))}},
    {"flight_num": "002", "origin": "Canada", "destination": "USA", "departure_time": "12:00 PM", "flight_type": "One Way", "seats": {"First Class": list(range(1, 21)), "Economy": list(range(21, 41))}},
    {"flight_num": "003", "origin": "USA", "destination": "Mexico", "departure_time": "2:00 PM", "flight_type": "Round Trip", "seats": {"First Class": list(range(1, 21)), "Economy": list(range(21, 41))}},
    {"flight_num": "004", "origin": "Mexico", "destination": "USA", "departure_time": "4:00 PM", "flight_type": "Round Trip", "seats": {"First Class": list(range(1, 21)), "Economy": list(range(21, 41))}}
]

passengers = []

def find_flight(flight_num):
    for flight in flights:
        if flight["flight_num"] == flight_num:
            return flight
    return None

def reserve_seat():
    flight_num = input("Enter flight number: ")
    flight = find_flight(flight_num)
    if flight:
        seat_type = input("Enter seat type (First Class or Economy): ")
        if seat_type in flight["seats"]:
            if len(flight["seats"][seat_type]) > 0:
                seat_num = flight["seats"][seat_type][0]
                flight["seats"][seat_type].remove(seat_num)
                name = input("Enter passenger name: ")
                passenger = {"name": name, "flight_num": flight_num, "seat_num": seat_num, "seat_type": seat_type}
                passengers.append(passenger)
                print("-" * 30)
                print("BOARDING PASS")
                print(f"Name: {name}")
                print(f"Flight: {flight_num}")
                print(f"Seat: {seat_type} {seat_num}")
                print("-" * 30)
            else:
                print("No seats available.")
        else:
            print("Invalid seat type.")
    else:
        print("Flight not found.")

def cancel_reservation():
    flight_num = input("Enter flight number: ")
    flight = find_flight(flight_num)
    if flight:
        seat_type = input("Enter seat type (First Class or Economy): ")
        if seat_type in flight["seats"]:
            seat_num = int(input("Enter seat number: "))
            if seat_num in flight["seats"][seat_type]:
                flight["seats"][seat_type].append(seat_num)
                flight["seats"][seat_type].sort()
                for passenger in passengers:
                    if passenger["flight_num"] == flight_num and passenger["seat_num"] == seat_num and passenger["seat_type"] == seat_type:
                        passengers.remove(passenger)
                        break
                print(f"Reservation for seat {seat_type} {seat_num} cancelled.")
            else:
                print("Seat not found.")
        else:
            print("Invalid seat type.")
    else:
        print("Flight not found.")

def show_available_seats():
    flight_num = input("Enter flight number: ")
    flight = find_flight(flight_num)
    if flight:
        print(f"Available seats for flight {flight_num}:")
        for seat_type, seats in flight["seats"].items():
            print(f"{seat_type}: {', '.join(map(str, seats))}")
    else:
        print("Flight not found.")

def show_menu():
    print("1. Reserve a seat")
    print("2. Cancel a reservation")
    print("3. Show available seats")
    print("4. Quit")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        reserve_seat()
    elif choice == "2":
        cancel_reservation()
    elif choice == "3":
        show_available_seats()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")