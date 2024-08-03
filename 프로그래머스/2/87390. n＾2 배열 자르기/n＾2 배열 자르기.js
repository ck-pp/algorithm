function solution(n, left, right) {
    var ans = [];
    for (let i = left; i < right+1; i++) {
        ans.push(Math.max(parseInt(i / n), i % n) + 1);
    }
    return ans;
}