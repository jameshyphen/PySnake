from domain.DomainController import DomainController

domainController = DomainController()


def Start():
    choice = 0
    while choice < 1 or choice > 2:
        print("1: Log in")
        print("2: Register")
        choice = int(input("Make a choice: "))
    if choice == 1:
        return Login()
    elif choice == 2:
        return Register()


def Login():
    choice = 0
    while choice is not 2:
        name = input("Username: ")
        password = input("Password: ")
        if domainController.loginPlayer(name, password):
            print("Successfully logged in.")
            break
        else:
            print("Username or password incorrect.")
            print("1: Retry")
            print("2: Return")
            choice = int(input("Make a choice: "))


def Register():
    choice = 0
    while choice < 1 or choice > 2:
        name = input("Username: ")
        password = input("Password: ")
        passwordConfirm = input("Confirm your password: ")
        if password == passwordConfirm:
            print("Successfully registered.")
            domainController.registerPlayer(name, password)
        else:
            print("Password confirmation is incorrect.")
            print("1: Retry")
            print("2: Return")
            choice = int(input("Make a choice: "))


# Start screen either login player or register
# By the end of this, player is instanced

while domainController.player is None:
    Start()

print(f"The player logged in is: {domainController.player.name}")
