function solution(sizes) {
    var ans = 0;
    var ws = [];
    var hs = [];
    for (let i = 0; i < sizes.length; i++) {
        sizes[i] = sizes[i].sort((a, b) => {return a-b});
        ws.push(sizes[i][0]);
        hs.push(sizes[i][1]);
    }
    ws.sort((a, b) => {return b-a});
    hs.sort((a, b) => {return b-a});
    return ws[0] * hs[0];
}