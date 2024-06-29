function solution(s){
    var stack = [];
    for (ch of s) {
        if (ch == '(')
            stack.push(ch)
        else {
            if (stack[stack.length -1] == '(')
                stack.pop()
            else
                return false;
        }
    }
    if (stack.length > 0)
        return false;
    else
        return true;
}