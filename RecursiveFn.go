func Recursive(number int) int {
    // base case here
    if number == 1 {
        return number
    }

    // general case, recursion used here
    return number + Recursive(number-1)
}

func Main() {
    answer := Recursive(4)
}
