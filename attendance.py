from itertools import permutations

def process(nod):
    if nod < 4:
        raise Exception('number of days needs to more than 3')
    min_days_to_attend = 4
    total_no_ways = 2 ** nod
    total_ways_to_miss = 2 ** (nod -1)
    invalid_ways = {( ('0',) * nod):1}
    possible_ways_to_present = nod - min_days_to_attend

    '''
    Generating all possible combinations for using 0's and 1's for valid days
    '''
    for p_day in range(1, possible_ways_to_present+1):
        absent_days = nod - p_day
        choices = '1'* p_day + '0' * absent_days
        perms = set(permutations(choices))

        for perm in perms:
            itert_counts = nod - min_days_to_attend - p_day  + 1
            stop_iter = False
            for count in range(itert_counts):
                consecutive_absent_days=step = nod - p_day - count
                limit = p_day + count + 1
                for index in range(limit):
                    sub_str = perm[index: index + step]
                    if sub_str.count('0') == consecutive_absent_days:
                        invalid_ways[perm] = invalid_ways.get(perm, 0) + 1
                        stop_iter = True
                        break
                if stop_iter:
                    break
    

    no_of_ways_to_attend = total_no_ways - len(invalid_ways)
    '''
    Invalidating all those ways where last day was absent.
    '''
    invalid_consecutive_days = sum(1 for way in invalid_ways if way[-1]=='0')
    probability = total_ways_to_miss - invalid_consecutive_days
    return f'{probability}/{no_of_ways_to_attend}'

#print(process(5))
#print(process(10))