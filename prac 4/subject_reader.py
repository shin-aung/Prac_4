"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    get_data(FILENAME)


def get_data(FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME, 'r')
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students")
    input_file.close()


main()