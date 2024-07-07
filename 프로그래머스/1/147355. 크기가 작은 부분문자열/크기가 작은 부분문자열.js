function solution(t, p) {
    var ans = 0;
    for (let i = 0; i < t.length - (p.length - 1); i++) {
        var num = parseInt(t.slice(i, i + p.length), 10);
        if (num <= parseInt(p, 10))
            ans += 1;
    }
    return ans;
}