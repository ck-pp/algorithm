function solution(n) {
    var ans = n.toString().split("");
    return ans.reverse().map((ch)=>parseInt(ch));
}