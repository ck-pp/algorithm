function solution(n) {
    for (let x = 2; x < n; x++) {
        if ((n-1) % x == 0) {
            return x
        }
    }
}