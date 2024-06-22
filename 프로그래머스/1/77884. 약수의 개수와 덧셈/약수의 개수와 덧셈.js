function solution(left, right) {
    var ans = 0;
    for (let i = left; i < right+1; i++) {
        if (Math.sqrt(i) % 1 == 0)
            ans -= i
        else
            ans += i
    }
    return ans;
}