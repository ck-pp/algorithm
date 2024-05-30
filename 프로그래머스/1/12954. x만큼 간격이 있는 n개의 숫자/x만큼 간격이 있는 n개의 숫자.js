function solution(x, n) {
    var ans = [];
    var m = 1;
    while (ans.length < n) {
        ans.push(x*m);
        m += 1
    }
    return ans;
}