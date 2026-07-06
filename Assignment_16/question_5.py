def display_reverse_order_with_while():
    i = 10
    reverse_order_list = list()
    while i >= 1:
        reverse_order_list.append(i)
        i -= 1

    return reverse_order_list

def display_reverse_order_with_range():
    reverse_order_list = list()
    for i in range(10, 0, -1):
        reverse_order_list.append(i)
    
    return reverse_order_list

def main():
    print("Revese order using while loop: ", display_reverse_order_with_while())
    print("Revese order using range: ", display_reverse_order_with_range())

if __name__ == "__main__":
    main()