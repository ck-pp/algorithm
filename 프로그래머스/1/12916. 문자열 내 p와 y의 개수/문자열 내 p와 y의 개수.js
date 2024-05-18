function solution(s){
    var p_cnt = 0;
    var y_cnt = 0;
    const arr = [...s];
    arr.forEach((ch)=>{
        if (ch === 'P' || ch === 'p') {
            p_cnt++;
        } else if (ch === 'Y' || ch === 'y') {
            y_cnt++;
        }
    })
    return p_cnt === y_cnt;
}