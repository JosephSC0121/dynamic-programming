package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type PathPoint struct {
	x, y int
}

var Triangle = [][]int{}

var PathMap = map[PathPoint]int{}

func LoadTriangle() {
	lines, _ := readLines()
	for _, line := range lines {
		fooSlice := []int{}
		for _, word := range strings.Fields(line) {
			foo, _ := strconv.Atoi(word)
			fooSlice = append(fooSlice, foo)
		}
		Triangle = append(Triangle, fooSlice)
	}
}

func readLines() ([]string, error) {
	file, err := os.Open("p067_triangle.txt")
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func ReducePaths(triangle [][]int, x, y int) (sum int) {
	curPoint := PathPoint{x, y}
	if val, ok := PathMap[curPoint]; ok {
		return val
	}

	curVal := triangle[y][x]
	var retVal int
	if y == 0 {
		retVal = curVal
	} else if x == 0 {
		retVal = curVal + ReducePaths(triangle, x, y-1)
	} else if x == len(triangle[y])-1 {
		retVal = curVal + ReducePaths(triangle, x-1, y-1)
	} else {
		left := ReducePaths(triangle, x-1, y-1)
		right := ReducePaths(triangle, x, y-1)
		if left >= right {
			retVal = curVal + left
		} else {
			retVal = curVal + right
		}
	}

	PathMap[curPoint] = retVal
	return retVal
}

func FindGreatestPath(triangle [][]int) (pathSum int) {
	y := len(triangle) - 1

	for i := 0; i < len(triangle[y]); i++ {
		pathVal := ReducePaths(triangle, i, y)
		if pathVal > pathSum {
			pathSum = pathVal
		}
	}

	return
}

func timeIt(start time.Time) {
	elapsed := time.Since(start)
	fmt.Printf("Completed in %s\n", elapsed)
}

func main() {
	LoadTriangle()
	defer timeIt(time.Now())
	fmt.Println("Max path val: ", FindGreatestPath(Triangle))

}
