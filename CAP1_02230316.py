#############################################################################
# Name: Kezang Dorji 
# Department: Electerical Engineering 
# Student Id: 02230316
##############################################################################
# Reference 
'''
1. https://www.learnpython.org
2. https://codekidz.ai/?gad_source=1&gclid=CjwKCAjwt-OwBhBnEiwAgwzrUrJx0NbkmWBqGKr1_g1Dx5qpjn8KSq7Rd5QysilQecZY6DMWs8V16RoCryAQAvD_BwE
'''
###############################################################################
# Solution
# Solution Score: 50223
# Number: 6
###############################################################################

# Function to read input from file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Read input from file
file_path = '/Users/Desktop/CAP1 Solution/input_6_cap1.txt'
lines = read_input(file_path)

# Initialize total score
total_score = 0

# Function to calculate score for each round
def calculate_score(player, opponent, result):
    choices = {'A': 1, 'B': 2, 'C': 3}
    results = {'X': 0, 'Y': 3, 'Z': 6}
    return choices[player] + results[result]

# Iterate through each line
for line in lines:
    # Extract opponent's choice and result
    opponent, result = line.strip().split()
    # Determine player's choice based on opponent's choice and result
    if opponent == "A":
        player = 'C' if result == "X" else ('A' if result == 'Y' else 'B')
    elif opponent == "B":
        player = 'A' if result == 'X' else ('B' if result == 'Y' else 'C')
    else:
        player = 'B' if result == 'X' else ('C' if result == 'Y' else 'A')
    # Calculate round score
    round_score = calculate_score(player, opponent, result)
    # Add round score to total
    total_score += round_score

# Print total score
print("Total Score:", total_score)
