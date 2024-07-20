function solution(food) {
    var food_arr = '';
    var food_arr_reverse = '';
    for (let i = 1; i < food.length; i++) {
        food_arr += `${i}`.repeat(parseInt(food[i]/2));
    }
    var food_arr_reverse = food_arr.split('').reverse();
    return food_arr + '0' + food_arr_reverse.join('');
}