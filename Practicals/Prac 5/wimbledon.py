"""
CP1404 Prac 5 - Wimbledon
Read wimbledon.csv and present champion win numbers and a list of countries champions were from
Estimate: 30 minutes
Actual:
"""
filename = "wimbledon.csv"


def main():
    """Read file and display champion data"""
    get_champion_data(filename)


def get_champion_data(filename):
    """Read champion data from the file"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        champion_data = []
        in_file.readline()
        for line in in_file:
            line = line.strip()
            parts = line.split(",")
        champion_data.append(parts)
    return champion_data


main()
