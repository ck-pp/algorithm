function solution(n) {
    var ans = 0;
    for (let i = 1; i <= parseInt(n**(1/2)); i++) {
        if (n % i == 0) {
            ans += (i + n/i)
            if (n / i == i) {
                ans -= i
            }
        }
    }
    return ans;
}