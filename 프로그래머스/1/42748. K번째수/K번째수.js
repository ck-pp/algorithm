function solution(array, commands) {
    var ans = [];
    for (c of commands) {
        var div_arr = array.slice(c[0]-1, c[1]);
        div_arr.sort((a, b) => a-b);
        ans.push(div_arr[c[2]-1]);
    }
    return ans;
}