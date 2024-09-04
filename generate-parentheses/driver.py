from solution import Solution


if __name__ == '__main__':
    s = Solution()

    n = 1
    print(f'{n=}:')
    print('\n'.join(s.generateParenthesis(n)))
    print()

    n = 2
    print(f'{n=}:')
    print('\n'.join(s.generateParenthesis(n)))
    print()

    n = 3
    print(f'{n=}:')
    print('\n'.join(s.generateParenthesis(n)))
    print()
