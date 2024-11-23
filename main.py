# John Elehwany
# Loyola CS151 PA04
# Professor Zee
# Due: November 22, 2024
# This program Lets the user analyze files and find repeating words in it.

# Purpose: Menu that displays choices for user and asks for input.
# Name: display_menu
# Parameters: none
# Return: choice
def display_menu():
    print("\nSelect an option:")
    print("1. Load a file")
    print("2. Count word in headlines")
    print("3. Write headlines to file")
    print("4. Average characters")
    print("5. Find shortest and longest headline")
    print("6. Quit")

    while True:
        try:
            choice = int(input("Enter choice (1-6): "))
            if choice >= 1 and choice <= 6:
                return choice
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

# Purpose: Reads filename after asking for input of it. Returns error message if it doesn't exist.
# Name: read_file
# Parameters: filename
# Return: headlines
def read_file(filename):
    try:
        file = open(filename, 'r')
        headlines = file.readlines()
        file.close()
        return headlines
    except:
        print("File not found.")
        return []

# Purpose: Counts a certain word in headlines.
# Name: count_word_in_headlines
# Parameters: headlines, word
# Return: count
def count_word_in_headlines(headlines, word):
    count = 0
    for headline in headlines:
        if word.lower() in headline.lower():
            count += 1
    return count

# Purpose: Writes headlines to a new file.
# Name: write_headlines_to_file
# Parameters: headlines, word, new_file
# Return: None
def write_headlines_to_file(headlines, word, new_file):
    file = open(new_file, 'w')
    for headline in headlines:
        if word.lower() in headline.lower():
            file.write(headline + "\n")
    file.close()

# Purpose: Gives average of average characters for each headline.
# Name: average_characters
# Parameters: headlines
# Return: total chars / len(headlines)
def average_characters(headlines):
    total_chars = 0
    for headline in headlines:
        total_chars += len(headline)
    if len(headlines) > 0:
        return total_chars / len(headlines)
    else:
        return 0

# Purpose: Finds the length of characters of a headline.
# Name: find_headline_lengths
# Parameters: headlines
# Return: shortest, longest
def find_headline_lengths(headlines):
    shortest = float('inf')
    longest = 0
    for headline in headlines:
        length = len(headline)
        if length < shortest:
            shortest = length
        if length > longest:
            longest = length
    return shortest, longest

# Purpose: Runs main program function.
# Name: main
# Parameters: none
# Return: none
def main():
    headlines = []
    while True:
        choice = display_menu()

        if choice == 1:
            filename = input("Enter the filename: ")
            headlines = read_file(filename)
        elif choice == 2:
            if not headlines:
                print("No file loaded.")
            else:
                word = input("Enter word: ")
                count = count_word_in_headlines(headlines, word)
                print(f"The word appears {count} times.")
        elif choice == 3:
            if not headlines:
                print("No file loaded.")
            else:
                word = input("Enter word: ")
                new_file = input("Enter new filename: ")
                write_headlines_to_file(headlines, word, new_file)
        elif choice == 4:
            if not headlines:
                print("No file loaded.")
            else:
                avg = average_characters(headlines)
                print(f"Avg characters: {avg:.2f}")
        elif choice == 5:
            if not headlines:
                print("No file loaded.")
            else:
                shortest, longest = find_headline_lengths(headlines)
                print(f"Shortest: {shortest}")
                print(f"Longest: {longest}")
        elif choice == 6:
            print("Goodbye!")
            break

main()
