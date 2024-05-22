function solution(n)
{
    var ans = 0;
    while (n > 0) {
        ans += (n % 10)
        n = parseInt(n / 10)
    }
    return ans;
}