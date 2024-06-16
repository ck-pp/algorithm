function solution(arr, divisor) {
    var ans = [];
    for (num of arr) {
        if (num % divisor == 0)
            ans.push(num);
    }
    if (ans.length < 1)
        ans.push(-1)
    
    // .sort()로 정렬하면 숫자가 아니라 문자로 변환되어서 예상한 결과와 달라진다!
    return ans.sort((a, b) => a - b);;
}