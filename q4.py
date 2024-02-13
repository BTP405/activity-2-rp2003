def stats_decorator(func):
    def wrapper(line):
        numbers = [int(num) for num in line.split()]
        count = len(numbers)
        total = sum(numbers)
        average = total / count
        maximum = max(numbers)
        
        print("Numbers read:", numbers)
        print("Count:", count)
        print("Average:", average)
        print("Maximum:", maximum)
        
        func(line)
    
    return wrapper

@stats_decorator
def process_line(line):
    pass  

def printStats(t):
    try:
        with open(t, 'r') as file:
            for line in file:
                process_line(line.strip())
    except FileNotFoundError:
        print("File not found.")



def main():
    printStats('data.txt')


if __name__ == "__main__":
    main()
