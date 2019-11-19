num_of_tests = int(input('Enter Number of Tests: '))

while num_of_tests:
    num_of_tests-=1
    a =  input('Enter first string: ')
    b = input('Enter Second string: ')
    b,a = [x for x in b], [x for x in a]
    for i in range(len(a)):
        try:
            if b[i] in a:
                print(True)
                break
        except:
            print(False)
            break
        