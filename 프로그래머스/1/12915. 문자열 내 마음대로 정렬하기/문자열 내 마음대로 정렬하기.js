function solution(strings, n) {
    strings.sort();
    return strings.sort((a, b) => a[n].charCodeAt() - b[n].charCodeAt());
}