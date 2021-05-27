package main

// CODE FOR SUBMISSION IS PLACED BELOW //

func trailingZeroes(n int) int {

	zeroNumber := 0
	for i := 5; n/i != 0; i*=5 {
		zeroNumber += n/i
	}

	return zeroNumber
}
