package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
    "sort"
)

func check(e error){
  if e != nil {
    panic(e)
  }
}

func main(){
  var result []int
  dat, err := os.ReadFile("day1p1.txt")
  check(err)
  elves := strings.Split(string(dat), "\n\n")
  for _, elf := range elves{
    var total int
    calories := strings.Split(elf, "\n")
    for _, cal := range calories{
      i, err := strconv.Atoi(cal)
      if err == nil{
        total += i
      }
    }
    result = append(result, total)
  }

  sort.Sort(sort.Reverse(sort.IntSlice(result)))
  fmt.Println("part 1:", result[0])
  fmt.Println("part 2:", result[0]+result[1]+result[2])
}
