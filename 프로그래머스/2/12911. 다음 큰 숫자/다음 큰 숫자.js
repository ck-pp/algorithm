function solution(n) {
    var n_next = n + 1;
    var n_bin_1 = n.toString(2).replaceAll('0', '').length;
    while (true) {
        var n_next_bin_1 = n_next.toString(2).replaceAll('0', '').length;
        if (n_next_bin_1 == n_bin_1)
            return n_next;
        else
            n_next += 1;
    }
}