function solution(a, b, n) {
    var ans = 0;
    var rem = 0;
    while (n >= a) {
        ans += (parseInt(n / a)) * b;
        n = n - a * (parseInt(n / a)) + (parseInt(n / a)) * b;
    }
    return ans;
}