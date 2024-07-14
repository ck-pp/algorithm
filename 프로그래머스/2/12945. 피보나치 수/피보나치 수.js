function solution(n) {
    var fibo = [0, 1];
    for (let i = 2; i < n+1; i++) {
        fibo.push((fibo[i-1] + fibo[i-2]) % 1234567);
    }
    return fibo[fibo.length-1] % 1234567;
}