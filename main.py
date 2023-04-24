import numpy as np
import graphviz


def dfs(matrix):
    visited = set()
    column = 0
    for i in range(len(set_edges)):
        if matrix[i][column] == '1' and column + 1 != len(set_nodes):
            visited.add(str(column + 1))
            for j in range(column + 1, len(set_nodes)):
                if matrix[i][j] == '1':
                    visited.add(str(j + 1))

    if visited == set_nodes:
        return True
    else:
        return False


match input("Directed = yes, not directed = no\n"):
    case 'yes':
        dot = graphviz.Digraph()
    case 'no':
        dot = graphviz.Graph()
    case _:
        print("Unknown command")
        exit('-1')

# Считываем матрицу из файла
matrix_of_incedence = []
nodes = 0
with open("matrix.txt") as matrix_file:
    for string in matrix_file:
        nodes = nodes + 1
        row = string.split()
        matrix_of_incedence.append(row)

set_nodes = set()
# Добавляем вершины
for i in range(nodes):
    set_nodes.add(str(i + 1))
    dot.node(str(i + 1))

# Записали матрицу
arr = np.array(matrix_of_incedence, str)
# Оттранспонировали ее
matrix = arr.transpose()

print(matrix)

# Добавляем ребра
set_edges = []
simple_graph = True
for string_of_nodes in matrix:
    one_node = True
    for i in range(len(string_of_nodes)):
        for j in range(i + 1, len(string_of_nodes)):
            if string_of_nodes[i] == string_of_nodes[j] == '1':
                set_edges.append(str(i + 1) + str(j + 1))
                if (str(j + 1) + str(i + 1)) in set_edges:
                    simple_graph = False
                one_node = False
    if one_node:
        simple_graph = False
        for i in range(len(string_of_nodes)):
            if string_of_nodes[i] == '1':
                set_edges.append(str(i + 1) + str(i + 1))

dot.edges(list(set_edges))

# Выводим пользователю граф
dot.render('doctest-output/round-table.gv', view=True)

# Проверка графа на связность по теореме в случае, если граф простой
if simple_graph:
    if (nodes - 1) * (nodes - 2) / 2 < len(set_edges):
        print("The Graph is linked")

# Проверка графа на связность, если он не простой
else:
    if dfs(matrix) is True:
        print("The Graph is linked")
    else:
        print("The Graph is not linked")
