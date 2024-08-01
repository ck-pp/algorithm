function solution(k, tangerine) {
    var sum = 0;
    var res = 0;
    var t_num = [];
    for (const t of tangerine) {
        t_num[t] = t_num[t] ? t_num[t] + 1 : 1;
    }
    
    t_num.sort((a, b) => b - a);
    
    for (const n of t_num) {
        sum += n;
        res += 1;
        if (sum >= k) return res;
    }
}