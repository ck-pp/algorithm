function solution(n)
{
    var ans = 0;
    while (n > 0) {
        if (n % 2 != 0) {
            ans += 1;
        }
        n = parseInt(n / 2);
    }
    return ans;
}