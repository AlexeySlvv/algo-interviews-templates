def get_number_of_good_pairs(numbers) -> int:
    # your code goes here
    d, cnt = {}, 0
    for num in numbers:
        m = num % 200
        if m in d:
            cnt += d[m]
            d[m] += 1
        else:
            d[m] = 1
    return cnt


n = int(input())
numbers = list(map(int, input().split()))
print(get_number_of_good_pairs(numbers))
