function solution(nums) {
    var set_n = new Set(nums);
    return Math.min(set_n.size, nums.length / 2);
}