# Implementation of the BFS and DFS algorithms
#
## Author: Gustavo Lima

## Beginnig of BFS algorithm
def bfs(translator,graphOri,treeBFS,visitedBFS):
    check = False                               # initialization of node knowledge check variable
    for i,neighbors in enumerate(graphOri):     # graph width check loop
        for j in neighbors:                          # neighbors check loop
            check = False                           # check variable reset
            for v in visitedBFS:                  # checking of previously visited nodes
                if (v == j):
                    check = True                    # if the node has already been visited, change the check variable to true and pass it to the next neighbor
            if(check == False):                     # if the node has not been visited
                visitedBFS.append(j)                 # add the node to the list of visitors
                treeBFS.append([translator[i],translator[j]])     #add the pair of connected nodes to the tree
#### End of BFS


## inicio do algoritmo DFS
def dfs(translator, graphOri,treeDFS,visitedDFS,origin):
    for j in graphOri[origin]:                 # neighbor check loop
        check = False                               # check variable
        for v in visitedDFS:                      # checking of previously visited nodes
            if (v == j):                            
                check = True                        # if the node has already been visited, the variable is changed to true and moves to the next neighbor
        if(check == False):                         #if the node has not been visited
            visitedDFS.append(j)                  #add the node to the list of visitors
            treeDFS.append([translator[origin],translator[j]])    #add the pair of connected nodes to the tree
            dfs(translator,graphOri,treeDFS,visitedDFS,j)    # recursively calls the search for the next in
### FIM algoritmo DFS 

## Initialization of variables
translator = ['A','B','C','D','E','F','G','H','I']   # translation variable from numerical to alphabetical nomenclature
graphOri = [[1,3],[3,4,5],[0,6,7],[2,5],[8],[8],[3,7,8],[],[]]
treeDFS = []
treeBFS = []
visitedDFS = [0]
visitedBFS = [0]
origin = 0   
##

## call of functions and print results
print('running bfs:')
bfs(translator,graphOri,treeBFS,visitedBFS)
print("Tree resulting from the BFS algorithm:")
print(treeBFS)
print('running dfs:')
dfs(translator,graphOri,treeDFS,visitedDFS,origin)
print("Tree resulting from the DFS algorithm:")
print(treeDFS)
