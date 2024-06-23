# Initial data for multiple users
users = {
    "1234": {"balance": 1000.00, "history": [], "aadhaar": None, "mobile": None},
    "5678": {"balance": 500.00, "history": [], "aadhaar": None, "mobile": None}
}

def check_balance(user):
    print(f"Your current balance is: ${user['balance']:.2f}")

def balance_enquiry(user):
    print(f"Your current balance is: ${user['balance']:.2f}")

def deposit_cash(user):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            user["balance"] += amount
            user["history"].append(f"Deposited ${amount:.2f}")
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid amount. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def withdraw_cash(user):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= user["balance"]:
            user["balance"] -= amount
            user["history"].append(f"Withdrew ${amount:.2f}")
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Invalid amount or insufficient balance. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def mini_statement(user):
    print("Mini Statement:")
    for transaction in user["history"]:
        print(transaction)

def change_pin(user, old_pin):
    old_pin_input = input("Enter your current PIN: ")
    if old_pin_input == old_pin:
        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Confirm your new PIN: ")
        if new_pin == confirm_pin:
            users[new_pin] = users.pop(old_pin)
            user["history"].append("PIN changed successfully")
            print("PIN changed successfully.")
        else:
            print("PIN confirmation does not match. Please try again.")
    else:
        print("Incorrect current PIN. Please try again.")

def link_aadhaar(user):
    aadhaar = input("Enter your Aadhaar number: ")
    if len(aadhaar) == 12 and aadhaar.isdigit():
        user["aadhaar"] = aadhaar
        user["history"].append(f"Aadhaar linked: {aadhaar}")
        print("Aadhaar linked successfully.")
    else:
        print("Invalid Aadhaar number. Please enter a 12-digit numeric value.")

def link_mobile(user):
    mobile = input("Enter your mobile number: ")
    if len(mobile) == 10 and mobile.isdigit():
        user["mobile"] = mobile
        user["history"].append(f"Mobile linked: {mobile}")
        print("Mobile number linked successfully.")
    else:
        print("Invalid mobile number. Please enter a 10-digit numeric value.")

def exit_atm():
    print("Thank you for using the ATM. Goodbye!")

def authenticate_user(max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        pin = input("Enter your PIN: ")
        if pin in users:
            return users[pin], pin
        else:
            print("Invalid PIN. Please try again.")
            attempts += 1
    print("Too many invalid attempts. Access denied.")
    return None, None

def atm_interface():
    print("Welcome to the ATM!")
    
    user, pin = authenticate_user()
    if not user:
        return
    
    while True:
        print("\nATM Menu:")
        print("1. Balance Enquiry")
        print("2. Deposit Cash")
        print("3. Withdrawal Cash")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Link Aadhaar")
        print("7. Link Mobile")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            balance_enquiry(user)
        elif choice == "2":
            deposit_cash(user)
        elif choice == "3":
            withdraw_cash(user)
        elif choice == "4":
            mini_statement(user)
        elif choice == "5":
            change_pin(user, pin)
        elif choice == "6":
            link_aadhaar(user)
        elif choice == "7":
            link_mobile(user)
        elif choice == "8":
            exit_atm()
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    atm_interface()
