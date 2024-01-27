from solution import Solution

if __name__ == '__main__':
    s = Solution()

    input_ = [[1,3], [2,6], [8,10], [15,18]]
    expected_output = [[1,6], [8,10], [15,18]]
    output = s.merge(input_)
    print(input_)
    print(output)
    assert output == expected_output

    input_ = [[1,4], [4,5]]
    expected_output = [[1,5]]
    output = s.merge(input_)
    print(input_)
    print(output)
    assert output == expected_output

    input_ = [[3,4], [1,7]]
    expected_output = [[1,7]]
    output = s.merge(input_)
    print(input_)
    print(output)
    assert output == expected_output
