from flask import Flask, jsonify, request
from db_utils import get_joined_date, book_different_room, delete_booking

app = Flask(__name__)


@app.route('/')
def get_home_page():
    res = {"HomePage": "Bingham"}
    return jsonify(res)


# Get the joined dates for Bingham members
@app.route('/joined_date/<joined_date>')  # by default route uses GET
def get_joined_date(joined_date):
    res = get_date(joined_date)
    return jsonify(res)


# Adding a different room for a member

@app.route('/joined_date/<int: member_id>', methods=['PUT'])
def book_different_room(member_id):
    booking = request.get_json()
    add_booking(
        date=booking['date'],
        room=booking['room'],
        time=booking['time'],
        member_id=member_id,
    )

    return jsonify(booking)


# Delete Member's Booking as he left the MembersClub
@app.route('/joined_date/<int: member_id>', methods=['DELETE'])
def delete_booking(member_id):
    deleted = delete_booking(member_id)
    return jsonify(deleted), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)
