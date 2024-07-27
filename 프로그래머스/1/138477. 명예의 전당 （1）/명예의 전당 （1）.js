function solution(k, score) {
    var ans = [];
    var top_score = score.slice(0, k);
    for (let i = 0; i < score.length; i++) {
        if (i < k) ans.push(Math.min(...score.slice(0, i+1)));
        else {
            if (Math.min(...top_score) < score[i]) {
                top_score.splice(top_score.indexOf(Math.min(...top_score)), 1);
                top_score.push(score[i]);
            }
            ans.push(Math.min(...top_score));
        }
    }
    return ans;
}