function solution(n) {
    var ans = 0;
    if (parseInt(n**(0.5)) ** 2 == n) {
        return (parseInt(n**(0.5)) + 1) ** 2
    }
    return -1;
}