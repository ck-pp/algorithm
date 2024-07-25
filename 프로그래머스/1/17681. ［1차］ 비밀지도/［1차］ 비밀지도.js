function solution(n, arr1, arr2) {
    var ans = [];
    for (let i = 0 ; i < n; i++) {
        var res_bin = (arr1[i]|arr2[i]).toString(2).padStart(n, '0');
        var res_conv = res_bin.replaceAll('1', '#').replaceAll('0', ' ');
        ans.push(res_conv);
    }
    return ans;
}