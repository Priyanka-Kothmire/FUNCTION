def max(numbers):
    max=numbers[0]
    i=0
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
            # print(max)
        i=i+1
    print(max)
max([3, 5, 7, 34, 2, 89, 2, 5])



