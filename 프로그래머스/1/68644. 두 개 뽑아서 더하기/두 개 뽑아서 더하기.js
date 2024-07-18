function solution(numbers) {
    var ans = [];
    for (let i = 0; i < numbers.length - 1; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            if (!ans.includes(numbers[i] + numbers[j]))
                ans.push(numbers[i] + numbers[j]);
        }
    }
    ans.sort((a, b) => a - b);
    return ans;
}