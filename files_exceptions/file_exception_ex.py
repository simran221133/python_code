# 10-8
files = ['/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/text_files/dogs.txt','/Users/Simran.Kaur6/Desktop/personal-projects/python3/files_exceptions/text_files/cats.txt']

for file in files:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError and IsADirectoryError:
        print("Please enter appropriate path for the file")
    else:
        print(contents)
