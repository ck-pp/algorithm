def solution(numbers, hand):
    answer = ''
    key = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    dict = {'L':'*', 'R':'#'}
    hand = hand.upper()

    for num in numbers:
        if num in [1, 4, 7] :
            answer += 'L'
            dict['L'] = str(num)
        elif num in [3, 6, 9]:
            answer += 'R'
            dict['R'] = str(num)
        else:
            pos = []
            left = []
            right = []
            for idxR in range(len(key)):
                if str(num) in key[idxR]:
                    pos.extend([idxR, key[idxR].index(str(num))])
                if dict['L'] in key[idxR]:
                    left.extend([idxR, key[idxR].index(dict['L'])])
                if dict['R'] in key[idxR]:
                    right.extend([idxR, key[idxR].index(dict['R'])])
            distanceL = abs(left[0]-pos[0]) + abs(left[1]-pos[1])
            distanceR = abs(right[0]-pos[0]) + abs(right[1]-pos[1])
            if distanceL < distanceR:
                answer += 'L'
                dict['L'] = str(num)
            elif distanceL > distanceR:
                answer += 'R'
                dict['R'] = str(num)
            else:
                answer+=hand[:1]
                dict[hand[:1]] = str(num)
    return answer