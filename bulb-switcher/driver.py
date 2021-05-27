import solution


if __name__ == '__main__':

    sol = solution.Solution()

    print(f'n=0 -> {sol.bulbSwitch(0)}')
    print(f'n=1 -> {sol.bulbSwitch(1)}')
    print(f'n=3 -> {sol.bulbSwitch(3)}')

    print(f'n=99999 -> {sol.bulbSwitch(99_999)}')
