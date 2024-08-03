function solution(cards1, cards2, goal) {
    var ans = '';
    cards1.reverse();
    cards2.reverse();
    for (word of goal) {
        if (word == cards1[cards1.length - 1]) cards1.pop();
        else if (word == cards2[cards2.length - 1]) cards2.pop();
        else return "No";
    }
    return "Yes";
}