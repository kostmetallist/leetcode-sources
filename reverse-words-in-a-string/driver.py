import solution


if __name__ == '__main__':

    testStr1 = "the sky is blue"
    testStr2 = "  hello world!  "
    testStr3 = "a good   example"
    sol = solution.Solution()

    print(sol.reverseWords(testStr1))
    print(sol.reverseWords(testStr2))
    print(sol.reverseWords(testStr3))
