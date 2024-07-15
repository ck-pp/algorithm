function solution(brown, yellow) {
    // 가로 길이 >= 세로 길이
    for (let i = 1; i < (yellow**(1/2)) + 1; i++) {
        var y_w = yellow / i;
        var y_h = i;
        if ((y_w + 2) * 2 + (y_h * 2) == brown) {
            return [y_w + 2, y_h + 2];
        } 
    }
}