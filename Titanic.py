"""Simple CLI tool to analyze ship_traffic_data.json."""

import json


def show_countries(all_data):
    """Return an alphabetically sorted list of all unique ship countries."""
    return sorted({ship["COUNTRY"] for ship in all_data["data"]})


def top_countries(all_data, num):
    """Return the top N countries with the highest number of ships."""
    country_counts = {}

    for ship in all_data["data"]:
        country = ship["COUNTRY"]
        country_counts[country] = country_counts.get(country, 0) + 1

    sorted_counts = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts[:num]


def show_help(menu_commands):
    """Print all available commands and their descriptions."""
    print("\nAvailable Commands:")
    for cmd, desc in menu_commands.items():
        print(f"{cmd}: {desc}")
    print()


def main():
    """Main loop of the CLI program. Loads data and processes user commands."""
    with open("ship_traffic_data.json", "r") as fileobj:
        raw_json = json.load(fileobj)      # raw_json ist ein STRING
        all_data = json.loads(raw_json)    # jetzt ein echtes Dictionary

    menu_commands = {
        "help": "List all available commands.",
        "show_countries": "Show all unique ship countries sorted alphabetically.",
        "top_countries <num>": "Show the top <num> countries with the most ships.",
        "q": "Quit the program."
    }

    print("-----------------------------------")
    print("Command Line Ships Traffic Analyzer")
    print("-----------------------------------")

    while True:
        user_input = input("Please enter command: ").strip()

        if user_input == "q":
            print("Goodbye!")
            break

        if user_input == "help":
            show_help(menu_commands)
            continue

        if user_input == "show_countries":
            for country in show_countries(all_data):
                print(country)
            print()
            continue

        if user_input.startswith("top_countries"):
            parts = user_input.split()

            if len(parts) != 2 or not parts[1].isdigit():
                print("Usage: top_countries <num>")
                continue

            num = int(parts[1])
            results = top_countries(all_data, num)

            print(f"\nTop {num} Countries:")
            for country, count in results:
                print(f"{country}: {count} ships")
            print()
            continue

        print("Please enter a valid command.\n")


if __name__ == "__main__":
    main()


