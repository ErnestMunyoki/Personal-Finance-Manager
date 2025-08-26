class Security:
    def __init__(self):
        self.password = "1234"

    def login(self):
        print("\n--- Security Login ---")
        entered = input("Enter password: ").strip()
        return entered == self.password