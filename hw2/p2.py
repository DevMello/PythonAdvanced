file_name = input("Enter the file name: ")

try:
    fhand= open(file_name)
    for line in fhand:
        upper_case_line = line.rstrip().upper()
        print(upper_case_line)
    fhand.close()
except FileNotFoundError:
    print("File not found", file_name)
except Exception as e:
    print("An error has occurred:", str(e))
