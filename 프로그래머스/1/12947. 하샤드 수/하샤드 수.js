function solution(x) {
    var sum_x = 0;
    var origin_x = x;
    while (x > 0) {
        sum_x += (x % 10);
        x = parseInt(x / 10);
    }
    return origin_x % sum_x == 0;
}