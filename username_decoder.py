# Author        : Ciaran O hOgain
# Version       : v1.0.0
# Description   : Encrypt a password using library

import base64
import sqlite3


def add_user():
    user_id = int(c.execute("SELECT user_id FROM usernames ORDER BY user_id DESC LIMIT 1").fetchone()[0]) + 1
    username = input("Enter your username: ")
    password = base64.b64encode(input("Enter your password: ").encode("utf-8"))

    c.execute('''INSERT INTO usernames (user_id, username, password) VALUES (?, ?, ?)''', (user_id, username, password))

    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect('test_database')
    c = conn.cursor()

    c.execute('''
              CREATE TABLE IF NOT EXISTS usernames
              ([user_id] INTEGER PRIMARY KEY, [username] TEXT, [password] TEXT)
              ''')

    conn.commit()
    check = input("Enter Y to add a username or N to search for a user\n")
    added = break_out_flag1 = break_out_flag2 = False

    while check != 'Y' or check != 'N' or added == True:
        if check == 'Y':
            add_user()
            added = True
            break
        elif check == 'N':
            request_name = input("Enter the username\n")
            user = c.execute("SELECT * FROM usernames;").fetchall()
            for i in range(0, len(user)):
                if user[i][1] == request_name:
                    print("Password is: {}\n".format(base64.decodebytes(user[i][2]).decode("utf-8")))
                    break_out_flag1 = True
                    break
                else:
                    print("This username is not in the database.")
                    check2 = input(" Would you like to add it? Enter Y/N")
                    while check2 != 'Y' or check2 != 'N':
                        if check2 == 'Y':
                            add_user()
                        elif check2 == 'N':
                            break_out_flag2 = True
                            break
                        else:
                            print("No option available, try again")
                            check2 = input()
                    if break_out_flag2:
                        break
            if break_out_flag1 or break_out_flag2:
                break
        else:
            print("No option available, try again")
            check = input()
