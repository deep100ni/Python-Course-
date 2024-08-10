def print_holo_square(size):
    print('*' * size)
    for i in range(2, size):
        print('*' + ' ' * (size - 2) + '*')
    print('*' * size)

size = int(input("Enter the size of the HoloSquare: "))
print_holo_square(size)