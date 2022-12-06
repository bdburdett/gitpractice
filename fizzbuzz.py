for i in range(1,100):
    if i % 3 ==0 or i % 5 == 0:
        print('fizzbuzz')
    if i % 5 == 0:
        print('buzz')
    if i % 3 == 0:
        print('fizz')
    else:
        print(i)