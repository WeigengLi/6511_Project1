import heapq

def is_solution(state, target):
    return state[0] == target or state[1] == target

def next_states(state, capacities):
    x, y = state
    results = []
    for i in range(len(capacities)):
        for j in range(len(capacities)):
            if i == j:
                continue
            if x == 0:
                results.append((capacities[i], y))
            elif y == 0:
                results.append((x, capacities[j]))
            elif x + y <= capacities[j]:
                results.append((0, x + y))
            elif x + y > capacities[j]:
                results.append((x + y - capacities[j], capacities[j]))
    return results

def h(state, target, capacities):
    x, y = state
    return max(target - x - y, 0)

def a_star(start, capacities, target):
    heap = [(h(start, target, capacities), 0, start, [])]
    visited = set()
    while heap:
        f, g, state, path = heapq.heappop(heap)
        if state in visited:
            continue
        visited.add(state)
        if is_solution(state, target):
            return (g, path + [state])
        for next_state in next_states(state, capacities):
            heapq.heappush(heap, (g + h(next_state, target, capacities), g + 1, next_state, path + [state]))
    return None

def read_input(filename):
    with open(filename) as f:
        capacities = list(map(int, f.readline().strip().split(',')))
        capacities.append(float('inf'))
        target = int(f.readline().strip())
    return capacities, target

def main():
    capacities, target = read_input('input.txt')
    result = a_star((0, 0), capacities, target)
    if not result:
        print('No solution found')
        return
    moves, path = result
    print(f'Number of moves: {moves}')
    print(f'Solution path: {path}')

if __name__ == '__main__':
    main()