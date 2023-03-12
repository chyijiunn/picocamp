def print_hello_one_by_one():
    print('Hello')

if __name__ == '__main__':
    while True:
        try:
            print_hello_one_by_one()
        except:
            continue