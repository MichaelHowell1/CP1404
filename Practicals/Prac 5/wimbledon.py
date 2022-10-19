"""
CP1404 Prac 5 - Wimbledon
Read wimbledon.csv and present champion win numbers and a list of countries champions were from
Estimate: 30 minutes
Actual: 52 minutes
"""


def main():
    """Read file and display champion data"""
    filename = "wimbledon.csv"

    champion_data = get_champion_data(filename)
    champion_name_to_wins, countries = convert_list(champion_data)
    display_stats(champion_name_to_wins, countries)


def get_champion_data(filename):
    """Read champion data from the file and display"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        champion_data = []
        in_file.readline()
        for line in in_file:
            line = line.strip()
            parts = line.split(",")
            champion_data.append(parts)
    return champion_data


def convert_list(champion_data):
    """Change champion data in list of lists into champion dictionary and extract set of countries from data"""
    champion_name_to_wins = {}
    countries = set()
    for champion in champion_data:
        countries.add(champion[1])
        try:
            champion_name_to_wins[champion[2]] += 1
        except KeyError:
            champion_name_to_wins[champion[2]] = 1
    return champion_name_to_wins, countries


def display_stats(champion_name_to_wins, countries):
    """Display champions names and their wins and countries"""
    print("Wimbledon Champions: ")
    max_word_length = max((len(name) for name in champion_name_to_wins))
    for name, wins in champion_name_to_wins.items():
        print(f"{name:{max_word_length}} {wins} wins")
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
