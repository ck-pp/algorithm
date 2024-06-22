function solution(left, right) {
    var ans = 0;
    for (let i = left; i < right+1; i++) {
        var num = 0;
        for (let j = 1; j < i+1; j++) {
            if (i % j == 0)
                num += 1
        }
        if (num % 2 == 0)
            ans += i
        else
            ans -= i
             }
    return ans;
}