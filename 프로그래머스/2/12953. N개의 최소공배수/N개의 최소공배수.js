function lcm(a, b) {
    return a * b / gcd(a, b);
}

function gcd(a, b) {
    while (true) {
        const r = a % b;
        if (r === 0) return b;
        a = b;
        b = r;
    }
}

function solution(arr) {
    arr.sort((a, b) => a - b);
    var lcm_v = arr[0];
    for (let i = 1; i < arr.length; i++) {
        lcm_v = lcm(lcm_v, arr[i]);
    }
    return lcm_v;
}