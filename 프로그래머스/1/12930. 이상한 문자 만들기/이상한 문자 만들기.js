function solution(s) {
    var ans = "";
    var words = s.split(" ");
    for (w of words) {
        for (let i = 0; i < w.length; i++) {
            if (i % 2 == 0)
                ans += w[i].toUpperCase();
            else
                ans += w[i].toLowerCase();
        }
        ans += ' ';
    }
    return ans.slice(0, s.length);
}