function solution(numbers) {
    var arr = [];
    for (let i = 0; i < numbers.length - 1; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            arr.push(numbers[i] + numbers[j]);
        }
    }
    const res_arr = [... new Set(arr)]
    return res_arr.sort((a, b) => a - b);
}