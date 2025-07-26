
file = open('sample.txt', 'r')
reading_lines1 = file.readlines(1)
print(f"line 1 : {reading_lines1}")
reading_lines2 = file.readlines(2)
print(f"line 2 : {reading_lines2}")

file.close()