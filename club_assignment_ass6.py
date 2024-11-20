import heapq
import copy

N = 4  # Example value for N (number of students/clubs)

class Node:
    def __init__(self, student, club, assigned, parent):
        self.parent = parent
        self.pathCost = 0
        self.cost = 0
        self.studentID = student
        self.clubID = club
        self.assigned = copy.deepcopy(assigned)
        if club != -1:
            self.assigned[club] = True

class CustomHeap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, (node.cost, node))

    def pop(self):
        if self.heap:
            _, node = heapq.heappop(self.heap)
            return node
        return None

def new_node(student, club, assigned, parent):
    return Node(student, club, assigned, parent)

def calculate_cost(cost_matrix, student, club, assigned):
    cost = 0
    available = [True] * N
    for i in range(student + 1, N):
        min_val, min_index = float('inf'), -1
        for j in range(N):
            if not assigned[j] and available[j] and cost_matrix[i][j] < min_val:
                min_index = j
                min_val = cost_matrix[i][j]
        cost += min_val
        available[min_index] = False
    return cost

def print_assignments(min_node):
    if min_node.parent is None:
        return
    print_assignments(min_node.parent)
    print("Assign Student {} to Club {}".format(chr(min_node.studentID + ord('A')), min_node.clubID))

def find_min_cost(cost_matrix):
    pq = CustomHeap()
    assigned = [False] * N
    root = new_node(-1, -1, assigned, None)
    root.pathCost = root.cost = 0
    root.studentID = -1

    pq.push(root)

    while True:
        min_node = pq.pop()
        student = min_node.studentID + 1

        if student == N:
            print_assignments(min_node)
            return min_node.cost

        for club in range(N):
            if not min_node.assigned[club]:
                child = new_node(student, club, min_node.assigned, min_node)
                child.pathCost = min_node.pathCost + cost_matrix[student][club]
                child.cost = child.pathCost + calculate_cost(cost_matrix, student, club, child.assigned)
                pq.push(child)

def get_cost_matrix():
    global N
    N = int(input("Enter the number of students/clubs: "))
    cost_matrix = []
    print("Enter the cost matrix row by row (space-separated):")
    for i in range(N):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        cost_matrix.append(row)
    return cost_matrix

if __name__ == "__main__":
    cost_matrix = get_cost_matrix()
    optimal_cost = find_min_cost(cost_matrix)
    if optimal_cost is not None:
        print("\nOptimal Cost is {}".format(optimal_cost))
    else:
        print("\nNo optimal solution found.")

