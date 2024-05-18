function solution(s){
    var p_cnt = 0;
    var y_cnt = 0;
    const arr = [...s.toUpperCase()];
    arr.forEach((ch)=>{
        if (ch === 'P') {
            p_cnt++;
        } else if (ch === 'Y') {
            y_cnt++;
        }
    })
    return p_cnt === y_cnt;
}