"""Simple CLI tool to analyze ship_traffic_data.json."""
import json


def show_countries(all_data):
    """Prints an alphabetically sorted list of all unique ship countries.
    Returns:
    bool: Always True, to keep the main loop running."""
    sorted_countries =  sorted({ship["COUNTRY"] for ship in all_data["data"]})
    for country in sorted_countries:
        print(country)
    return True


def top_countries(all_data, num):
    """Prints the top N countries with the highest number of ships.
    Returns:
    bool: Always True, to keep the main loop running."""
    country_counts = {}
    for ship in all_data["data"]:
        country = ship["COUNTRY"]
        country_counts[country] = country_counts.get(country, 0) + 1
    sorted_counts = (
        sorted(country_counts.items(), key=lambda x: x[1], reverse=True))
    results = sorted_counts[:num]
    print(f"\nTop {num} Countries:")
    for country, count in results:
        print(f"{country}: {count} ships")
    print()
    return True


def ships_by_types(all_data):
    """Print the number of ships for each ship type based on TYPE_SUMMARY.
    Returns:
    bool: Always True, to keep the main loop running."""
    type_counts = {}
    for ship in all_data["data"]:
        ship_type = ship.get("TYPE_SUMMARY")
        type_counts[ship_type] = type_counts.get(ship_type, 0) + 1
    sorted_types = (
        sorted(type_counts.items(), key=lambda x: x[1], reverse=True))
    print("\nShips by Type:")
    for ship_type, count in sorted_types:
        print(f"{ship_type}: {count} ships")
    print()
    return True


def show_help(_):
    """Print all available commands.
    Returns:
    bool: Always True, to keep the main loop running."""
    print("\nAvailable Commands:")
    print("help - Show this help message")
    print("show_countries - List all unique countries")
    print("top_countries <num> - Show top N countries with most ships")
    print("ships_by_types - Show the number of ships for each ship type")
    print("q - Quit the program\n")
    return True

def quit_program(_):
    """Quit the program.
    Returns:
    bool: Always False to quit the program."""
    print("Goodbye!")
    return False

def main():
    """Main loop of the CLI program. Loads data and processes user commands."""
    with open("ship_traffic_data.json", "r") as fileobj:
        raw_json = json.load(fileobj)      # raw_json ist ein STRING
        all_data = json.loads(raw_json)    # jetzt ein echtes Dictionary

    menu_commands = {
        "help": show_help,
        "show_countries": show_countries,
        "top_countries": top_countries,
        "ships_by_types": ships_by_types,
        "q": quit_program
    }

    print("-----------------------------------")
    print("Command Line Ships Traffic Analyzer")
    print("-----------------------------------")
    status = True
    while status:
        user_input = input("Please enter command: ").strip().lower()
        if user_input.startswith("top_countries"):
            parts = user_input.split()
            if len(parts) != 2 or not parts[1].isdigit():
                print("Enter top_countries <num>")
                continue
            num = int(parts[1])
            menu_commands[parts[0]](all_data, num)
            continue
        try:
            status = menu_commands[user_input](all_data)
        except KeyError:
            print("Please enter a valid command.\n")


if __name__ == "__main__":
    main()


