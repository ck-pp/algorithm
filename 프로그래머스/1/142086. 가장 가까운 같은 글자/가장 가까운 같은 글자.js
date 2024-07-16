function solution(s) {
    var res = [];
    var stack = [];
    for (word of s) {
        var value = -1;
        if (stack.includes(word)) {
            value = stack.length - stack.lastIndexOf(word);
        }
        stack.push(word);
        res.push(value);
    }
    return res;
}