def solution(int_array):
    max_elem = max(int_array, default=0)
    if max_elem < 1:
        return 1
    int_array = set(int_array)
    all_ints = set(range(1, max_elem + 1))
    diff_set = all_ints - int_array
    if len(diff_set) == 0:
        return max_elem + 1
    return min(diff_set)

print(solution([11, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-3]))
