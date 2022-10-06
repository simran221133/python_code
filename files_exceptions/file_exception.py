file_path = '/Users/Simran.Kaur6/Desktop/personal-projects/python3/test.txt'

try:
    with open(file_path) as f:
        contents = f.read()
        print(contents)        
except FileNotFoundError:
    print("File not present")
