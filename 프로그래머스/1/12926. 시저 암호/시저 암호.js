function solution(s, n) {
    var ans = '';
    var A_ascii = 'A'.charCodeAt()
    var a_ascii = 'a'.charCodeAt()
    for (w of s) {
        if (w == ' ')
            ans += ' ';
        else {
            var w_n_ascii = w.charCodeAt() + n
            // 소문자인지 체크
            var compare = /^[a-z]+$/.test(w) ? a_ascii : A_ascii;
            console.log(w_n_ascii, compare + 25)
            ans += (String.fromCharCode(w_n_ascii > compare + 25 ? w_n_ascii - 26 : w_n_ascii ))
        }
    }
    return ans;
}