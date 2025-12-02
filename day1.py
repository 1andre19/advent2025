res = 0
with open('input', 'r') as f:
    pos = 50
    for line in f:
        direction = line[0]
        rotations = int(line[1:])

        # print(line, f" which is in direction of {direction} and by {rotations}")

        # (50 - 12)

        for i in range(rotations):
            if direction == "L":
                pos = ((pos - 1) % 100)
            else:
                pos = ((pos + 1) % 100)

            if pos == 0: 
                res += 1



print(f"result = {res}")
