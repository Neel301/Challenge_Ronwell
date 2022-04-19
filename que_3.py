from collections import defaultdict
def solution(N, A, B):
    # write your code in Python 3.6
    pass
    graph = defaultdict(set)
    for i in range(len(A)):
        graph[A[i]].add(B[i])
        graph[B[i]].add(A[i])
    print(graph)
    for i in range(2,N+1):
        if i-1 not in graph[i]:
            return False
    return True

print(solution(4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1]))
print(solution(4, [1, 2, 1, 3], [2, 4, 3, 4]))
print(solution(6, [2, 4, 5, 3], [3, 5, 6, 4]))
print(solution(3, [1, 3], [2, 2]))