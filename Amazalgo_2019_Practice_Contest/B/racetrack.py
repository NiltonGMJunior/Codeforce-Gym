#   Codeforces
#   #Amazalgo 2019 Practice Contest - B   -  Racetrack
#   https://codeforces.com/gym/102063/problem/B
#   14/01/2019
#   Nilton G. M. Junior

if __name__ == '__main__':
    a, b = list(map(int, input().split()))

    k_a = 1
    k_b = 1

    while k_a * a != k_b * b:
        if k_a * a < k_b * b:
            k_a += 1
        else:
            k_b += 1

    print(k_a * a)

    # The following works but takes too long
    # for num in range(min([a, b]), a * b + 1):
    #     if num % a == 0 and num % b == 0:
    #         print(num)
    #         break
