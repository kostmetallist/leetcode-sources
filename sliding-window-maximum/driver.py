from solution import Solution


if __name__ == '__main__':
    
    s = Solution()

    nums = [1, 3, -1, -3, 2, 1, 6, 7]
    k = 3
    print(s.maxSlidingWindow(nums, k))

    nums = [42]
    k = 1
    print(s.maxSlidingWindow(nums, k))
