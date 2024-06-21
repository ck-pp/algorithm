function solution(a, b) {
    var ans = 0;
    for (let idx = 0; idx < a.length; idx++) 
            ans += (a[idx] * b[idx])
    return ans;
}