function solution(arr) {
    var min = arr[0];
    for (n of arr) {
        if (n < min)
            min = n
    }
    arr.splice(arr.indexOf(min), 1)
    return arr.length > 0 ? arr : [-1];
}