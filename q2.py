import matplotlib.pyplot as plt

def graphSnowfall(t):
    snowfall_ranges = {'0-10': 0, '11-20': 0, '21-30': 0, '31-40': 0, '41-50': 0}

    # Read data from the file and aggregate values into ranges
    with open(t, 'r') as file:
        for line in file:
            snowfall = int(line.strip())
            if snowfall <= 10:
                snowfall_ranges['0-10'] += 1
            elif snowfall <= 20:
                snowfall_ranges['11-20'] += 1
            elif snowfall <= 30:
                snowfall_ranges['21-30'] += 1
            elif snowfall <= 40:
                snowfall_ranges['31-40'] += 1
            else:
                snowfall_ranges['41-50'] += 1

    labels = list(snowfall_ranges.keys())
    values = list(snowfall_ranges.values())

    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Snowfall Ranges (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation')
    plt.show()


def main():
    graphSnowfall('snowfall_data.txt')


if __name__ == "__main__":
    main()

