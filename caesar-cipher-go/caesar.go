package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"unicode"
)

func main() {
	var plaintext string
	var key int

	// More than two arguments
	if len(os.Args) > 2 {
		fmt.Println("Usage: ./caesar k")
		os.Exit(1)
	}

	// Lack of key argument
	if len(os.Args) == 1 {
		fmt.Println("Usage: ./caesar k")
		os.Exit(1)
	}

	// Gets key
	key, _ = strconv.Atoi(os.Args[1])

	// Verify if key is an non negative integer
	if key <= 0 {
		fmt.Println("Usage: ./caesar k")
		os.Exit(1)
	}

	// Create alphabetic indexes
	var lower_alphabet_index []rune
	var upper_alphabet_index []rune
	for i := 'a'; i <= 'z'; i++ {
		lower_alphabet_index = append(lower_alphabet_index, i)
	}
	for i := 'A'; i <= 'Z'; i++ {
		upper_alphabet_index = append(upper_alphabet_index, i)
	}

	// Read plaintext
	fmt.Print("plaintext: ")
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		plaintext = scanner.Text()
	}

	// Cipher it!
	for _, c := range plaintext {
		if unicode.IsUpper(c) {
			index_key := c - 65
			new_key := math.Mod(
				float64(int(index_key)+key),
				float64(26),
			)

			new_char := upper_alphabet_index[int(new_key)]
			fmt.Printf("%c", new_char)
		} else if unicode.IsLower(c) {
			index_key := c - 97
			new_key := math.Mod(
				float64(int(index_key)+key),
				float64(26),
			)

			new_char := lower_alphabet_index[int(new_key)]
			fmt.Printf("%c", new_char)
		} else {
			fmt.Print(string(c))
		}
	}
}
