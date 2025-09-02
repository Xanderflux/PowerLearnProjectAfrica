class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, message, number):
        print(f"Sending '{message}' to {number}...")

class Android(Smartphone):
    def __init__(self, brand, model, storage, os_version):
        super().__init__(brand, model, storage)
        self.os_version = os_version

    def take_screenshot(self):
        print("Taking screenshot...")

class iPhone(Smartphone):
    def __init__(self, brand, model, storage, ios_version):
        super().__init__(brand, model, storage)
        self.ios_version = ios_version

    def take_screenshot(self):
        print("Taking screenshot...")

def main():
    android = Android("Samsung", "Galaxy S22", "128GB", "11.0")
    iphone = iPhone("Apple", "iPhone 13", "256GB", "15.2")

    android.make_call("123-456-7890")
    android.send_message("Hello!", "123-456-7890")
    android.take_screenshot()

    iphone.make_call("987-654-3210")
    iphone.send_message("Hi!", "987-654-3210")
    iphone.take_screenshot()

if __name__ == "__main__":
    main()

