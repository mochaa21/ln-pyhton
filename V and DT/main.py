# Abyy

# function

def confirm_action():
    while True:
        response = input("Do you want to continue? (y/n) -> ").strip().lower()

        # logic
        if response in ['y', 'yes']:
            return True
        if response in ['n', 'no']:
            return False
        print("Invalid input. Please enter 'y' or 'n'.")

# need insert: v, i, f, b

# v
name = input("Your name: ")
email = input("Your valid email: ")

# i
age = int(input("Your age: "))


# result of v and i
print(f"Your submission has been successfully recorded...\nName: {name}\nEmail: {email}\nAge: {age}")

# f
price = 10.99

if confirm_action():
    budget = int(input("Input your budget: "))

    def confirm_action_store():
        while True:
            response = input(f"Do you want to buy? the price is ${price} (y/n) -> ").strip().lower()

            # logic
            if response in ['y', 'yes']:
                return True
            if response in ['n', 'no']:
                return False
            print("Invalid input. Please enter 'y' or 'n'.")

    if confirm_action_store():
        budget = budget - price
        print(f"Success! Your budget now is ${budget}")
    else:
        print('Action Cancelled.')

else:
    print('Action Cancelled.')

