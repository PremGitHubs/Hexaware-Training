def login():
    """
    Simple login page application that accepts Name and ID
    """
    print("=" * 50)
    print("         WELCOME TO LOGIN PAGE")
    print("=" * 50)
    
    # Accept user input
    name = input("\nEnter your Name: ").strip()
    user_id = input("Enter your ID: ").strip()
    
    # Validate inputs
    if not name or not user_id:
        print("\n❌ Error: Name and ID cannot be empty!")
        return False
    
    # Display login confirmation
    print("\n" + "=" * 50)
    print("         LOGIN SUCCESSFUL")
    print("=" * 50)
    print(f"Welcome, {name}!")
    print(f"Your ID: {user_id}")
    print("=" * 50 + "\n")
    
    return True


if __name__ == "__main__":
    login()
