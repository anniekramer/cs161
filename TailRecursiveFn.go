func TailRecursiveFn(number int, product int) int {
    product = product + number

    if number == 1 {
        return product
    }

    return TailRecursiveFn(number-1, product)
}

func main() {
    answer := TailRecursiveFn(4,0)
}
