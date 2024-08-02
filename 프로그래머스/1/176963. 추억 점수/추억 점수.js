function solution(name, yearning, photo) {
    var ans = [];
    var name_idx = new Map();
    name.forEach((name, idx) => {
        name_idx.set(name, idx);
    })
    for (arr of photo) {
        var sum = 0;
        for (n of arr) {
            // hasOwnProperty()는 일반 객체의 프로토타입 메서드
            // Map에서는 has() 메서드를 사용하여 키의 존재 여부를 확인한다.
            if (name_idx.has(n)) sum += yearning[name_idx.get(n)];
        }
        ans.push(sum);
    }
    return ans;
}