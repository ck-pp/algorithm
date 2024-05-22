function solution(n) {
    var ans = [];
    // var ans = n.toString().split("");
    // return ans.reverse().map((ch)=>parseInt(ch));
    while (n > 0) {
        ans.push(n % 10)
        n = parseInt(n / 10)
    }
    return ans;
}