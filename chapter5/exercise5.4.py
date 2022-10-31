'''Exercise 5.4'''

def arithmetic_sum(a, d, n):
    counter = 0 #i, j, k
    sum_list = []
    sum_list.append(a)
    while counter != n-1:
        a += d
        sum_list.append(a)
        counter += 1
    return (sum(sum_list))

print(arithmetic_sum(3, 2, 15))
