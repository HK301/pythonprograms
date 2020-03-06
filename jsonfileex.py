import jsonex

jsonex.create_user(12, 'Siva')
jsonex.update_user(10, "Hari")

switcher = {
    1:jsonex.create_user,
    2:jsonex.update_user,
}
print("Please enter below option to do operation\n 1. create user\n 2. update user.")
user_option = int(input("Enter a option >>>\n"))

# Get the fuction from switcher dictionaryb

func = switcher.get(user_option, lambda: "Invalid option")

# Execute the function
user_id = input("Enter user id >>>\n")
user_name = input("Enter user name >>>\n")

func(user_id, user_name)
