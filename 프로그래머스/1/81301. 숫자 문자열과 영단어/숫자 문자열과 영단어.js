function solution(s) {
    var eng_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    
    for (let i = 0; i < eng_num.length; i++) {
        s = s.replaceAll(eng_num[i], i);
    }
    
    return parseInt(s);
}