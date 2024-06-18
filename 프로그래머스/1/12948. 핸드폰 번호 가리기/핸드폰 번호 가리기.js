function solution(phone_number) {
    var ans = '';
    for (let i = 0; i < phone_number.length; i++) {
        if (i < phone_number.length - 4)
            ans += '*'
        else
            ans += phone_number[i]
    }
    
    return ans;
}