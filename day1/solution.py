with open(input.txt) as file:
    while line := file.readline():
        print(line.rstrip())