function solution(numbers) {
    var sum = 45;
    for (n of numbers) {
        sum -= n
    }
    return sum;
}