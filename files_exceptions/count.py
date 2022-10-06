# function to check if the file exists and provide a count for character in the txt file
def file_check(file_paths):
    try:
        # try block inserted right before the program tried to open a file
        with open(file_path) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Please provide correct path to the file {file_path}\n")
    else:
        new = contents.split()
        count = len(new)
        print(f"Count of all characters is {count} in the file {file_path}\n")

# assigning a list of paths
file_paths = ['/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/python.txt',
'/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/names.txt',
'/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/random.txt',
'/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/reasons.txt']

# looping through each path 
for file_path in file_paths:
    # calling the function on file_paths
    file_check(file_paths)



