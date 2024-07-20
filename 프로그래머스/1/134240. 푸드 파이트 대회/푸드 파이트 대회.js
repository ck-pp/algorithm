function solution(food) {
    var food_arr = '';
    for (let i = 1; i < food.length; i++) {
        food_arr += `${i}`.repeat(parseInt(food[i]/2));
    }
    
    return food_arr + '0' + [...food_arr].reverse().join('');
}