function solution(A,B){
    var ans = 0;
    A.sort((a, b) => {return a - b})
    B.sort((a, b) => {return b - a})
    for (let i = 0; i < A.length; i++)
        ans += A[i] * B[i]
    return ans;
}