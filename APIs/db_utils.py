import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

    def get_joined_date(date):
        availability = []
        try:
            db_name = 'Bingham'
            db_connection = connect_to_db(db_name)
            cur = db_connection.cursor()
            print("Connected to DB: %s" % db_name)

            query = """
                SELECT  member_id, surname, joined_date
                FROM MembersClub 
                WHERE joined_date= "2019-06-06";
                """

            cur.execute(query, (date,))
            for (member_id, surname, joined_date) in cur:
                availability.append({"member_id": member_id, "surname": surname, "joined_date": joined_date})

            cur.close()
        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            if db_connection:
                db_connection.close()
                print("DB connection is closed")

        return availability

    def book_different_room(member_id, date, room, time, member):
        try:
            db_name = 'Bingham'
            db_connection = connect_to_db(db_name)
            cur = db_connection.cursor()
            print("Connected to DB: %s" % db_name)

            query = """
                UPDATE  room
                FROM MembersClub
                SET room = "Restaurant"
                WHERE member_id = 305 AND member_id = 457;
                """.format(member_id=member_id, date=date, room=room, time=time, member=member)

            cur.execute(query)
            db_connection.commit()
            cur.close()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

        finally:
            if db_connection:
                db_connection.close()
                print("DB connection is closed")


def delete_booking(member_id):
    try:
        db_name = 'Bingham'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            DELETE  member_id, surname, phone_number, joined_date, room 
            FROM MembersClub
            WHERE member_id = 184 AND surname= "PARMA";
            """.format(member=member_id)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == '__main__':
    run()
