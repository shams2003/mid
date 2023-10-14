class Star_Cinema:
    def __init__(self):
        self._hall_list = []

    def entry_hall(self, hall):
        if isinstance(hall, Hall):
            self._hall_list.append(hall)
        else:
            print("Invalid input. Please provide an object of the Hall class.")

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = []  # 2D matrix for seats information
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()

    def _initialize_seats(self):
        for _ in range(self._rows):
            row = ['free' for _ in range(self._cols)]
            self._seats.append(row)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)

    def book_seats(self, show_id, seats_to_book):
        for show in self._show_list:
            if show[0] == show_id:
                for seat in seats_to_book:
                    row, col = seat
                    if 1 <= row <= self._rows and 1 <= col <= self._cols:
                        if self._seats[row - 1][col - 1] == 'free':
                            self._seats[row - 1][col - 1] = 'booked'
                        else:
                            print(f"Seat {row}-{col} is already booked.")
                    else:
                        print(f"Invalid seat: {row}-{col}")
                return
        print("Invalid show ID.")

    def view_show_list(self):
        for show in self._show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        for show in self._show_list:
            if show[0] == show_id:
                for row in range(self._rows):
                    available_seats = [col + 1 for col in range(self._cols) if self._seats[row][col] == 'free']
                    if available_seats:
                        print(f"Row {row + 1}: Seats {', '.join(map(str, available_seats))} are available.")
                    else:
                        print(f"Row {row + 1}: No available seats.")
                return
        print("Invalid show ID.")

# Example usage:
if __name__ == "__main__":
    cinema = Star_Cinema()

    while True:
        print("\nOptions:")
        print("1. Create Hall and Entry Show")
        print("2. Book Seats")
        print("3. View Show List")
        print("4. View Available Seats")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            hall_no = input("Enter the hall number: ")
            hall = Hall(rows, cols, hall_no)
            cinema.entry_hall(hall)
            print(f"Hall {hall_no} has been created.")
        elif choice == '2':
            show_id = input("Enter the show ID: ")
            seats_to_book = input("Enter the seats to book (e.g., 1-2 3-4): ").split()
            seats_to_book = [(int(seat.split('-')[0]), int(seat.split('-')[1])) for seat in seats_to_book]
            for hall in cinema._hall_list:
                hall.book_seats(show_id, seats_to_book)
        elif choice == '3':
            for hall in cinema._hall_list:
                hall.view_show_list()
        elif choice == '4':
            show_id = input("Enter the show ID: ")
            for hall in cinema._hall_list:
                hall.view_available_seats(show_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")
