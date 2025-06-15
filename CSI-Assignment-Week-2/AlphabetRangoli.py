def print_rangoli(size):
    width = 4 * size - 3  # total width

    # Top half including middle line
    for i in range(size):
        s = ''
        # Left part (from size-1 to size-1-i)
        for j in range(size - 1, size - 1 - i, -1):
            s += chr(97 + j) + '-'
        # Middle + right part (from size-1-i to size-1)
        s += chr(97 + size - 1 - i)
        for j in range(size - i, size):
            s += '-' + chr(97 + j)
        # Print line centered with hyphens
        print(s.center(width, '-'))

    # Bottom half (excluding middle line)
    for i in range(size - 2, -1, -1):
        s = ''
        for j in range(size - 1, size - 1 - i, -1):
            s += chr(97 + j) + '-'
        s += chr(97 + size - 1 - i)
        for j in range(size - i, size):
            s += '-' + chr(97 + j)
        print(s.center(width, '-'))