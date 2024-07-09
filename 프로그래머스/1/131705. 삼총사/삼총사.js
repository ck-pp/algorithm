function solution(number) {
    var ans = 0;
    const getCombinations = function (arr, selectNumber) {
        const results = [];
        if (selectNumber === 1) return arr.map((el) => [el]); 
        // n개중에서 1개 선택할 때(nC1), 바로 모든 배열의 원소 return

        arr.forEach((fixed, index, origin) => {
            const rest = origin.slice(index + 1); 
            const combinations = getCombinations(rest, selectNumber - 1); 
            const attached = combinations.map((el) => [fixed, ...el]); 
            results.push(...attached); 
        });

        return results;
    }
    
    var comb = getCombinations(number, 3);
    for (c of comb) {
        var sum = 0;
        c.forEach((num) => {
            sum += num;
        })
        if (sum == 0)
            ans += 1;
    }
    return ans;
}