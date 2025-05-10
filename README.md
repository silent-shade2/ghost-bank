import random
import json
import os

# User Data (load from a file or initialize)
user_data = {
    "name": "Ghost Seeker",
    "balance": 500,
    "debt": 0,
    "savings": 0,
    "investments": 0,
    "spending_history": [],
    "vault_locked": True,
    "time_capsules": [],
    "challenges_completed": []
}

# Load user data from a JSON file
def load_user_data():
    global user_data
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            user_data = json.load(file)

# Save user data to a JSON file
def save_user_data():
    with open("user_data.json", "w") as file:
        json.dump(user_data, file)

# Display the main menu
def main_menu():
    print("\nWelcome to Ghost Bank!")
    print("1. Phantom's Financial Diary")
    print("2. Ghostly Budget Tracker")
    print("3. Spectral Wealth Forecast")
    print("4. The Forgotten Vault")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        time_capsule()
    elif choice == "2":
        budget_tracker()
    elif choice == "3":
        wealth_forecast()
    elif choice == "4":
        forgotten_vault()
    elif choice == "5":
        exit_game()
    else:
        print("Invalid choice! Try again.")
        main_menu()

# Phantom's Financial Diary (Time Capsule)
def time_capsule():
    print("\nPhantom's Financial Diary")
    entry = input("Enter your financial thoughts: ")
    
    if entry.strip() == "":
        print("You must enter some text!")
        time_capsule()
    else:
        user_data["time_capsules"].append(entry)
        print(f"Your entry has been saved! You wrote: {entry}")
        save_user_data()
        main_menu()

# Ghostly Budget Tracker
def budget_tracker():
    print("\nGhostly Budget Tracker")
    print(f"Current Balance: £{user_data['balance']}")
    print(f"Debt: £{user_data['debt']}")
    print(f"Savings: £{user_data['savings']}")
    main_menu()

# Spectral Wealth Forecast
def wealth_forecast():
    print("\nSpectral Wealth Forecast")
    forecast = f"In 6 months, you will have £{user_data['balance'] + random.randint(0, 1000)}."
    print(forecast)
    main_menu()

# The Forgotten Vault (Locked until puzzle is solved)
def forgotten_vault():
    print("\nThe Forgotten Vault")
    if user_data['vault_locked']:
        print("The Vault is Locked! Solve the mystery to unlock it.")
        vault_puzzle()
    else:
        print(f"The Vault contains £{user_data['savings']} in hidden funds.")
        main_menu()

# Vault puzzle: user needs to solve a math question to unlock
def vault_puzzle():
    print("Solve this math puzzle to unlock the vault:")
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    answer = num1 + num2
    
    user_answer = input(f"What is {num1} + {num2}? ")

    if user_answer.isdigit() and int(user_answer) == answer:
        print("Correct! The Vault is now unlocked.")
        user_data['vault_locked'] = False
        user_data['savings'] = random.randint(100, 1000)  # Vault contains some savings now
        save_user_data()
        main_menu()
    else:
        print("Incorrect answer. Try again.")
        vault_puzzle()

# Exit the game
def exit_game():
    print("Thank you for playing! Your progress has been saved.")
    save_user_data()
    exit()

# Load data on game start
load_user_data()

# Start the game
main_menu()
