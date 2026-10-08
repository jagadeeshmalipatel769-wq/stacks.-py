plates = []

plates.append(1)
plates.append(2)
plates.append(3)

print("Top of stack:", plates[-1])

while plates:
    print("Popped:", plates.pop())