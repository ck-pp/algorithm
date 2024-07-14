function solution(s)
{
    var stack = []
    var i = 0;
    while (i < s.length) {
        if (stack.length > 0 && stack[stack.length - 1] == s[i]) {
            stack.pop();
        } else {
            stack.push(s[i]);
        }
        i += 1;
    }
    return stack.length == 0 ? 1 : 0;
}