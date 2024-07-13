function solution(s, n) {
    var upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var lower = "abcdefghijklmnopqrstuvwxyz";
    var ans = '';

    for(let i = 0; i < s.length; i++){
        var w = s[i];
        if(w == ' ') {
            ans += ' '; 
            continue;
        }
        var textArr = upper.includes(w) ? upper : lower;
        var idx = textArr.indexOf(w)+n;
        if(idx >= textArr.length) idx -= textArr.length;
        ans += textArr[idx];
    }
    return ans;
}