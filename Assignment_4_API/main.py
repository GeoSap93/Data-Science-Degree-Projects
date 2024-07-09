import requests
import json
from pprint import pprint


def get_joined_date(joined_date):
    result = requests.get(
        'http://127.0.0.1:5001/joined_date/{}'.format(joined_date),
        headers={'content-type': 'application/json'}
    )
    return result.json()


def book_different_room(member_id, date, room, time, member):
    booking = {
        "date": date,
        "room": room,
        "time": time,
        "member": member,
    }

    result = requests.put(
        'http://127.0.0.1:5001/joined_date/{}'.format(member_id),
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )

    return result.json()


def delete_booking(member_id):
    result = requests.delete(
        'http://127.0.0.1:5001/joined_date/{}'.format(member_id),
        headers={'content-type': 'application/json'}
    )
    return result.json()


print(result)  # Brings back a response 200


#print(result.json) # Brings the data printed

def run():
    print('############################################################')
    print('Hello, welcome to Bingham, the best MembersClub in Richmond!')
    print('############################################################')
    print()
    date = input('What date you would like to work at Bingham (YYYY-MM-DD): ')
    print()
    slots = {
        'Monday': ['9-10', '10-11', '11-12', '12-13', '13-14', '14-15'],
        'Tuesday': ['9-10', '10-11', '11-12', '12-13', '13-14', '14-15'],
        'Wednesday': ['9-10', '10-11', '11-12', '12-13', '13-14', '14-15'],
        'Thursday': ['9-10', '10-11', '11-12', '12-13', '13-14', '14-15'],
        'Friday': ['9-10', '10-11', '11-12', '12-13', '13-14', '14-15'],
        'Saturday': ['9-10', '10-11', '11-12', '12-13', '13-14', '14-15'],
        'Sunday': ['9-10', '10-11', '11-12', '12-13', '13-14', '14-15']
    }
    print('####### AVAILABILITY #######')
    pprint(slots)

    room_booking = input('What room would you like to book (Library/Restaurant/Parlour)?  ')

    book = room_booking == 'y'

    if book:
        member = input('Please enter your member id: ')
        surname = input('Enter your surname: ')
        time = input('Choose time based on availability (e.g 10-11): ')
        drink = input('Kindly let us know what drink would you like upon your arrival: ')
        add_new_booking(date, time, surname, member, drink)
        print("Booking is Successful. We look forward to seeing you soon!")
        print()
        slots = get_available_bookings(date)
        display_availability(slots)

    print()
    print('We hope you enjoy your time in Bingham!')


if __name__ == '__main__':
    run()
