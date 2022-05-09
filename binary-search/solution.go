package main

// CODE FOR SUBMISSION IS PLACED BELOW //

func search(nums []int, target int) int {

	var examIndex int
	result := -1
	begin, end := 0, len(nums)-1

	for begin <= end {

		examIndex = begin + (end-begin)/2
		if nums[examIndex] == target {
			result = examIndex
			break

		} else if nums[examIndex] < target {
			begin = examIndex + 1

		} else {
			end = examIndex - 1
		}
	}

	return result
}
