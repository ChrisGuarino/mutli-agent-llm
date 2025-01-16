from command_parsing import parse_command
from dispatcher import dispatch_command 


def main():
    while True:
        # Example user input
        command = input("What do you want to do? ")

        # Parse the command
        parsed_command = parse_command(command)

        # Execute the parsed command
        dispatch_command(parsed_command)


if __name__ == "__main__":
    main() 




