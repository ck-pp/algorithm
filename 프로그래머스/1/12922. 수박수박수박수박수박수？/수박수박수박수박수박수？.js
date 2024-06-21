function solution(n) {
    var ans = '';
    let word = ["수", "박"];
    for (let i = 0; i < n; i++)
        ans += word[i%2];
    return ans;
}