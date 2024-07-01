function solution(s) {
    var words = s.split(' ');
    for (let i = 0; i < words.length; i++) {
        if (words[i].length > 0) {
            if (isNaN(Number(words[i][0])))
                words[i] = words[i][0].toUpperCase() + words[i].slice(1).toLowerCase();
            else
                words[i] = words[i][0] + words[i].slice(1).toLowerCase();
        }
    }
    return words.join(' ');
}