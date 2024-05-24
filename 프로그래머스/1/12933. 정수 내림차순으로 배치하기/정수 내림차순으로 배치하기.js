function solution(n) {
    var ans = [];
    while (n > 0) {
        ans.push(n % 10)
        n = parseInt(n / 10)
    }
    return parseInt(ans.sort().reverse().join(""));
}