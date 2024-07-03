function solution(n, m) {
    var ans = [];
    var multi_v = m * n
    while (n > 0) {
        var t = m % n;
        m = n;
        n = t;
    }
    return [m, multi_v / m];
}