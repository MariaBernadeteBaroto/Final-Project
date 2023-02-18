import sys

from heapq import heapify, heappush, heappop

def dijsktra(graph,src,dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf,'pred':[]},
    'B':{'cost':inf,'pred':[]},
    'C':{'cost':inf,'pred':[]},
    'D':{'cost':inf,'pred':[]},
    'E':{'cost':inf,'pred':[]},
    'F':{'cost':inf,'pred':[]},
    'G':{'cost':inf,'pred':[]},
    'H':{'cost':inf,'pred':[]},
    'I':{'cost':inf,'pred':[]},
    'J':{'cost':inf,'pred':[]}
    }
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(9):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost']+graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        temp = min_heap[0][1]
        distance = str(node_data[dest]['cost'])
        path = str(node_data[dest]['pred'] + list(dest))

    print('The shortest path is: ')
    if 'A' in path:
        print('Main Gate')
    if 'B' in path:
        print('Gymnasium')
    if 'C' in path:
        print('Oval')
    if 'D' in path:
        print('Swimming Pool')
    if 'E' in path:
        print('Mabini Shrine')
    if 'F' in path:
        print('Library')
    if 'G' in path:
        print('Chapel')
    if 'H' in path:
        print('Main Building')
    if 'I' in path:
        print('Laboratory Highschool')
    if 'J' in path:
        print('Charlie Building')

    
if __name__=="__main__":
    graph = {
        'A':{'B':6, 'C':7},
        'B':{'A':6, 'C':15, 'D':13},
        'C':{'A':7, 'B':15, 'D':20, 'E':10},
        'D':{'B':13, 'C':20, 'E':17, 'F':11, 'G':21},
        'E':{'C':10, 'D':17, 'G':12},
        'F':{'D':11, 'G':18, 'H':14},
        'G':{'D':21, 'E':10, 'F':18, 'H':22, 'I':9},
        'H':{'F':14, 'G':22, 'I':9, 'J':5},
        'I':{'G':9, 'H':19, 'J':4},
        'J':{'H':5, 'I':4}
    }


    user_input1 = input('Enter starting point: ')
    if user_input1 == 'Main Gate':
        source = 'A'
    if user_input1 == 'Gymnasium':
        source = 'B'
    if user_input1 == 'Oval':
        source = 'C'
    if user_input1 == 'Swimming Pool':
        source = 'D'
    if user_input1 == 'Mabini Shrine':
        source = 'E'
    if user_input1 == 'Library':
        source = 'F'
    if user_input1 == 'Chapel':
        source = 'G'
    if user_input1 == 'Main Building':
        source = 'H'
    if user_input1 == 'Laboratory Highschool':
        source = 'I'
    if user_input1 == 'Charlie Building':
        source = 'J'

    user_input2 = input('Enter destination: ')
    if user_input2 == 'Main Gate':
        destination = 'A'
    if user_input2 == 'Gymnasium':
        destination = 'B'
    if user_input2 == 'Oval':
        destination = 'C'
    if user_input2 == 'Swimming Pool':
        destination = 'D'
    if user_input2 == 'Mabini Shrine':
        destination = 'E'
    if user_input2 == 'Library':
        destination = 'F'
    if user_input2 == 'Chapel':
       destination = 'G'
    if user_input2 == 'Main Building':
        destination = 'H'
    if user_input2 == 'Laboratory Highschool':
        destination = 'I'
    if user_input2 == 'Charlie Building':
        destination = 'J'


    dijsktra(graph,source,destination)