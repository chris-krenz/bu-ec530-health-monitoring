"""
Client for forming and submitting SQL queries.
"""

from requests import post, get, delete
import sanitizer

url = "http://localhost:8000/"

while '0' != (action := input("Enter number: \n\t"
                              "0. Exit... \n\t"
                              "1. GET \n\t"
                              "2. POST \n\t"
                              "3. DELETE \n")):
    print(sanitizer.sanitizer(action))

    while '0' != (table := input("Enter number: \n\t"
                                 "0. Go Back... \n\t"
                                 "1. USERS \n\t"
                                 "2. DEVICES \n")):
        print(sanitizer.sanitizer(table))

        match table:
            case '1':
                table = 'users'
                break
            case '2':
                table = 'devices'
                break
            case '0':
                table = 0
                break

    if table == 0:
        continue

    match action:

        case '1':  # GET
            uid = input("Enter User ID: ")
            try:
                if not uid.isdigit():
                    raise TypeError('You must provide an integer id...')
                print(get(url + table + '/' + uid).json())
            except Exception as e:
                print(f"ERROR: Failed to get user with ID {uid}:", e)

        case '2':  # POST
            uid = input("Enter User ID: ")
            name = input("Enter User Name: ")
            try:
                if not uid.isdigit():
                    raise TypeError('You must provide an integer id...')
                print(sanitizer.sanitizer(name))
                print(post(url + table + '/' + uid, json={"name": name}))
            except Exception as e:
                print(f"ERROR: Failed to create user:", e)

        case '3':  # DELETE
            uid = input("Enter User ID: ")
            if not uid.isdigit():
                raise TypeError('You must provide an integer id...')
            try:
                print(delete(url + table + '/' + uid))
            except Exception as e:
                print(f"ERROR: Failed to delete user with ID {uid}:", e)

        case '0':  # EXIT
            break
        case _:
            print("Can't interpret user input...")
