package main

import (
	"fmt"
	"strings"
)

func main() {
	var height int
	fmt.Print("Height: ")
	fmt.Scan(&height)

	i := 0

	for i <= height {
		if i != 0 {
			fmt.Print(strings.Repeat(" ", height-i))
			fmt.Println(strings.Repeat("#", i+1))
		}
		i++
	}

}
