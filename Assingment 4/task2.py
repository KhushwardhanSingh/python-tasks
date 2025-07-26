

with open ('output.txt', 'w') as file:
    a = input("Enter text to write to the file: ")
    print("data written to file successfully.")
    file.write(a + '\n')
    b =input ("enter append text to file: ")
    print("data appended to file successfully.")
    file.write(b + '\n')