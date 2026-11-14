
def nights_stayed(days):
    if not isinstance(days, str):
        return 0

    parts = days.split('-')

    if len(parts) != 2:
        return 0

    try:
        check_in = int(parts[0])
        check_out = int(parts[1])
        return check_out - check_in
    except ValueError:
        return 0


def room_floor(room_code):
    if not isinstance(room_code, str):
        return 0

    parts = room_code.split('-')

    if len(parts) != 2 or not parts[1]:
        return 0

    if not parts[1][0].isdigit():
        return 0

    return int(parts[1][0])


def booking_label(names_csv):
    if not isinstance(names_csv, str):
        return "Unknown +0"

    names = [n.strip() for n in names_csv.split(',') if n.strip()]

    if not names:
        return "Unknown +0"

    lead = names[0]
    return lead[0].upper() + lead[1:] + " +" + str(len(names) - 1)


def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    result = nights_stayed(user_input)
    print("Nights:", result)

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    result = room_floor(user_input)
    print("Floor:", result)

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    result = booking_label(user_input)
    print("Booking Label:", result)


if __name__ == "__main__":
    main()
