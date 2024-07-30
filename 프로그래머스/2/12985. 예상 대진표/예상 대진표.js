function solution(n,a,b)
{
    var ans = 0;
    while (Math.ceil(a/2) != Math.ceil(b/2)) {
        a = Math.ceil(a/2)
        b = Math.ceil(b/2)
        ans += 1
    }
    return ans + 1;
}