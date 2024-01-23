import solution


if __name__ == '__main__':
    s = solution.Solution()

    prices_1 = [7, 1, 5, 3, 6, 4]
    print(prices_1)
    print(s.maxProfit(prices_1))
    print()

    prices_2 = [7, 6, 4, 3, 1]
    print(prices_2)
    print(s.maxProfit(prices_2))
    print()

    prices_3 = [7]
    print(prices_3)
    print(s.maxProfit(prices_3))
    print()
