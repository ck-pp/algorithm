function solution(arr)
{
    var ans = [];
    for (s of arr) {
        if (ans.length == 0 || (ans && ans[ans.length-1] != s))
            ans.push(s);
    }
    return ans;
}