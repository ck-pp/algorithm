function solution(s) {
    var ans = '';
    var s_num = s.split(' ').map(Number).sort((a, b) => a - b);
    return `${s_num[0]} ${s_num[s_num.length-1]}`;
}