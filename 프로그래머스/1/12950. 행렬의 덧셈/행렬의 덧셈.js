function solution(arr1, arr2) {
    var ans = [];
    for (let i = 0; i < arr1.length; i++) {
        var list = [];
        for (let j = 0; j < arr1[i].length; j++) {
            list.push(arr1[i][j] + arr2[i][j])
        }
        ans.push(list);
    }
    return ans;
}