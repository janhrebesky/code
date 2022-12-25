command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car has already started")
        else:
            command = True
            print("The car is going")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print("The car has stopped")
    elif command == "help":
        print("""
start- to start the game
stop- to stop the game
quit- to quit the game
            """)
    elif command == "quit":
        break
    else:
        print("I dont understand that!")
