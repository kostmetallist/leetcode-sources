package main

import (
	"bufio"
	"fmt"
	"os"
)

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
