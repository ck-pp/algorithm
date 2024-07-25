function solution(people, limit) {
    var ans = 0;
    people.sort((a, b) => b - a); // 내림차순
    for (let i = 0; i < people.length; i++) {
        ans += 1;
        if (people[i] + people[people.length - 1] <= limit) {
            people.pop();
        }
    }
    return ans;
}