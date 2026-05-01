from api import get_country
from formatter import format_country, format_history, compare_countries, format_stats
from db import CountryDB

db = CountryDB()


def show_menu():
    print("""
================= Country CLI ======================
search <country>        → Fetch country details
history                 → Show past searches
compare <c1> <c2>       → Compare two countries
stats                   → Show most searched region
exit                    → Quit the program
====================================================
""")


def main():
    while True:
        show_menu()

        command = input(">> ").strip().lower()

        if command.startswith("search"):
            name = command.split(" ", 1)[1]

            try:
                country = get_country(name)
                format_country(country)
                db.save(country)
            except Exception as e:
                print(f"Error: {e}")

        elif command == "history":
            rows = db.get_history()
            format_history(rows)

        elif command.startswith("compare"):
            try:
                query = command[len("compare"):].strip()

                if " vs " not in query:
                    raise ValueError

                c1, c2 = query.split(" vs ", 1)

                c1 = c1.strip()
                c2 = c2.strip()

                country1 = get_country(c1)
                country2 = get_country(c2)

                compare_countries(country1, country2)

            except:
                print("Usage: compare <country1> vs <country2>\n")

        elif command == "stats":
            stat = db.get_stats()
            format_stats(stat)

        elif command in ["exit", "quit"]:
            print("Goodbye")
            break

        else:
            print("""
Commands:
- search <country>
- history
- compare <country1> <country2>
- stats
- exit
""")

if __name__ == "__main__":
    main()