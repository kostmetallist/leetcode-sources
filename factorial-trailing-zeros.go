package main

import (
	"bufio"
	"fmt"
	"os"
	// "strconv"
)

func trailingZeroes(n int) int {

	zeroNumber := 0
	for i := 5; n/i != 0; i*=5 {
		zeroNumber += n/i
	}

	return zeroNumber
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("enter n: ")
	input, _ := reader.ReadString('\n')
	var value int
	_, err := fmt.Sscan(input, &value)
	if (err == nil) {
		result := trailingZeroes(value)
		fmt.Println("factorial trailing spaces is", result)
	} else {
		fmt.Println("error while converting input to int")
	}
}