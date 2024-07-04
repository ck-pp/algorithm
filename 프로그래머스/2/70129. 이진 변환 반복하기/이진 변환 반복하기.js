function solution(s) {
    var conv_cnt = 0;
    var remove_cnt = 0;
    while (s != '1') {
        remove_cnt += (s.split('0').length - 1);
        conversion_s = s.replaceAll('0', '');
        s = conversion_s.length.toString(2);
        conv_cnt += 1;
    }
    return [conv_cnt, remove_cnt];
}