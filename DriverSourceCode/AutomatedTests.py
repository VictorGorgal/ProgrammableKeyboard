def test1():
    return True


def test2():
    return True


list_of_tests = [test1, test2]

for idx, test in enumerate(list_of_tests):
    print(f'>>Running test nº{idx+1}', end=' ')

    result = 'Fail'
    if test():
        result = 'Success'

    print(f' | {result}')
