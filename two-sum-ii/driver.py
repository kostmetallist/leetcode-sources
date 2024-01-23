import solution


if __name__ == '__main__':

    s = solution.Solution()

    print(s.twoSum(
        [2, 7, 11, 15],
        9
    ))

    print(s.twoSum(
        [2, 3, 4],
        6
    ))

    print(s.twoSum(
        [-1, 0],
        -1
    ))

    print(s.twoSum(
        [-8, 2, 3, 4, 1000],
        7
    ))
