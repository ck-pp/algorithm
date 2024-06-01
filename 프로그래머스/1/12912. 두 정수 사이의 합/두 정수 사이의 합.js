function solution(a, b) {
    var sum = 0;
    if (a > b) {
        [a, b] = [b, a];
    }
    for (let i = a; i < b+1; i++) {
        sum += i;
    }
    return sum;
}