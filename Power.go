func Power(int x, int n) int {
    // base case here
    if n == 0 {
        return 1
    // general case here
    } else {
        return x * Power(x, (n-1))
    }
}


func Main() {
    answer := Power(3,2)
}
