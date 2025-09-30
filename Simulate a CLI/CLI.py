
class CLI:
    def __init__(self):
        self.storage = {}

    def set(self, key, val):
        try:
            self.storage[key] = val
        except Exception as e:
            print(e)
        else:
            print(f"Successfully saved key {key} and value {val}.")

    def get(self, key):
        if key in self.storage:
            val = self.storage[key]
            print(f"The value for key {key} is: {val}.")
        else:
            print(f"Cannot get key {key}, it does not exist!")

    def delete(self, key):
        if key in self.storage:
            del self.storage[key]
            print(f"Successfully deleted key {key}")
        else:
            print(f"Cannot delete key {key}, it does not exist!")


    def cleanup(self):
        exit(0)

    def start(self):
        while True:
            user_input = input("Please select a command (set, get, del, or exit): ")

            match user_input.strip():
                case "set":
                    params = input("Please enter a space-separated key and value, i.e 3 10: ").strip().split()
                    if len(params) != 2:
                        print("Please enter only a key and a value!")
                    else:
                        key, val = params
                        self.set(key, val)

                case "get":
                    wanted_key = input("Enter the key to search for: ").strip()
                    self.get(wanted_key)

                case "del":
                    to_delete = input("Enter the key you want to delete: ").strip()
                    self.delete(to_delete)

                case "exit":
                    self.cleanup()

                case _:
                    print("Invalid command, try again.")


app = CLI()
app.start()
