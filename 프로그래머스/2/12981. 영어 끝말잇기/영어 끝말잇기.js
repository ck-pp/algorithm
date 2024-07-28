function solution(n, words) {
    var st = [words[0]];
    for (let i = 1; i < words.length; i++) {
        if ((st[st.length - 1].slice(-1) != words[i][0]) || (st.indexOf(words[i]) > -1)) {
            return [i % n + 1, parseInt(i / n) + 1];
    }
        st.push(words[i]);
    }
    return [0, 0];
}