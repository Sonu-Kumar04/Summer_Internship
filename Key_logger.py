import logging

# Configure the logger
logging.basicConfig(filename="user_keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def main():
    print("Welcome to the User Keylogger!")

    while True:
        user_input = input("Enter something: ")

        # Log the user input
        logging.info(user_input)

        # Check if the user wants to quit
        if user_input.lower() == "q":
            break

    print("Keylog saved in 'user_keylog.txt'.")

if __name__ == "__main__":
    main()
