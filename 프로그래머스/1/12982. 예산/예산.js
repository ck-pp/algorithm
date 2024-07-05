function solution(d, budget) {
    var ans = 0;
    var cumulative_sum = 0;
    d.sort((a, b) => a - b);
    for (num of d) {
        ans += 1;
        cumulative_sum += num;
        if (cumulative_sum >= budget) {
            if (cumulative_sum > budget)
                ans -= 1;
            break;
        }
    }
    return ans;
}