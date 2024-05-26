function solution(arr) {
    var sum = 0;
    for (n of arr) {
        sum += n;
    }
    return sum / arr.length;
}