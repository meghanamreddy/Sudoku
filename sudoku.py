'''
Created on 15-May-2014

@author: Meghana M Reddy
'''

k = []
import math
def add_node(node):
    if not node in graph :
        graph[node] = ()

def add_directed_edge(node1, node2):
    flag = 0
    if node1 not in graph :
        add_node(node1)
    if node2 not in graph :
        add_node(node2)
    for i in graph[node1]:
        if i == node2:
            flag = 1
            break
    if flag != 1:
        graph[node1] += (node2,)

        
def add_edge(node1, node2):
    if node1 != node2:
        add_directed_edge(node1, node2)
        add_directed_edge(node2, node1)
        
def ruleone(g, K, L, matrix):
    for i in range(0, 9):
        for j in range(0, 9):
            if matrix[i][j] == 1 and K[i][j] == '-':
                for m in range(0,9):
                    if L[i][j][m] == 1:
                        K[i][j] = str(m + 1)
                        for u in g[str(i)+str(j)]:
                            if K[int(u[0])][int(u[1])] == '-':
                                if L[int(u[0])][int(u[1])][m] == 1:
                                    L[int(u[0])][int(u[1])][m] = 0
                                    matrix[int(u[0])][int(u[1])] -= 1
                        break

def ruletwo(g, K, L, matrix):
    for i in range(0, 9):
        for w in range(0,9):
            count = 0
            for j in range(0,9):
            
                
                if L[j][i][w] == 1 and K[j][i]=='-' :
                        count =count + 1
                        J=j
                            
            if count == 1:
                    K[J][i] = str(w + 1)
                    matrix[J][i] = 1
                    for n in range(0, 9):
                        L[J][i][n] = 0
                    L[J][i][w] = 1
                    
                    for v in g[str(J)+str(i)]:
                        if K[int(v[0])][int(v[1])] == '-':
                            if L[int(v[0])][int(v[1])][w] == 1:
                                L[int(v[0])][int(v[1])][w] = 0
                                matrix[int(v[0])][int(v[1])] -= 1 
                          
    
    for i in range(0, 9):
        for w in range(0,9):
            count = 0
            for j in range(0,9):
            
                
                if L[i][j][w] == 1 and K[i][j]=='-' :
                            count =count + 1
                            J=j
                            
            if count == 1:
                    K[i][J] = str(w + 1)
                    matrix[i][J] = 1
                    for n in range(0, 9):
                        L[i][J][n] = 0
                    L[i][J][w] = 1
                    
                    for v in g[str(i)+str(J)]:
                        if K[int(v[0])][int(v[1])] == '-':
                            if L[int(v[0])][int(v[1])][w] == 1:
                                L[int(v[0])][int(v[1])][w] = 0
                                matrix[int(v[0])][int(v[1])] -= 1 
                          

    
    for i in range(0, 9):
        for j in range(0,9):
            x = int(math.floor(float(i/3)) * 3)
            y = int(math.floor(float(j/3)) * 3)
            
            for w in range(0,9):
                count = 0
                for f in range(x, x+3):
                    for s in range(y, y+3):
                        if L[f][s][w] == 1 and K[f][s]=='-' :
                            count =count + 1
                            F=f
                            S=s
                if count == 1:
                        K[F][S] = str(w + 1)
                        matrix[F][S] = 1
                        for n in range(0, 9):
                            L[F][S][n] = 0
                        L[F][S][w] = 1
                        
                        for v in g[str(F)+str(S)]:
                            if K[int(v[0])][int(v[1])] == '-':
                                if L[int(v[0])][int(v[1])][w] == 1:
                                    L[int(v[0])][int(v[1])][w] = 0
                                    matrix[int(v[0])][int(v[1])] -= 1 


def rulethree(g, K, L, matrix):
    for num1 in range(0, 9):
        for num2 in range(0, 9):
            if num1 == num2:
                continue
            for i in range(0, 9):
                count = 0
                flag = 0
                for j in range(0, 9):
                    if (L[i][j][num1] == 1 and L[i][j][num2] == 0) or (L[i][j][num1] == 0 and L[i][j][num2] == 1):
                        flag = 1
                    elif L[i][j][num1] == 1 and L[i][j][num2] == 1:
                        count += 1
                        if count == 1:
                            one_ind = j
                        elif count == 2:
                            two_ind = j
                if count == 2 and flag == 0: 
                    for j in range(0, 9):
                        if j == num1 or j == num2:
                            continue
                        L[i][one_ind][j] = 0
                        L[i][two_ind][j] = 0
                    matrix[i][one_ind] = 2
                    matrix[i][two_ind] = 2
        
    for num1 in range(0, 9):
        for num2 in range(0, 9):
            if num1 == num2:
                continue
            for i in range(0, 9):
                count = 0
                flag = 0
                for j in range(0, 9):
                    if (L[j][i][num1] == 1 and L[j][i][num2] == 0) or (L[j][i][num1] == 0 and L[j][i][num2] == 1):
                        flag = 1
                    elif L[j][i][num1] == 1 and L[j][i][num2] == 1:
                        count += 1
                        if count == 1:
                            one_ind = j
                        elif count == 2:
                            two_ind = j
                if count == 2 and flag == 0:
                    for j in range(0, 9):
                        if j == num1 or j == num2:
                            continue
                        L[one_ind][i][j] = 0
                        L[two_ind][i][j] = 0
                    matrix[one_ind][i] = 2
                    matrix[two_ind][i] = 2
                    
    for num1 in range(0, 9):
        for num2 in range(0, 9):
            if num1 == num2:
                continue
            for I in range(0, 9, 3):
                for J in range(0, 9, 3):
                    count = 0
                    flag = 0
                    for i in range(I, I+3):
                        for j in range(J, J+3):
                            if (L[i][j][num1] == 1 and L[i][j][num2] == 0) or (L[i][j][num1] == 0 and L[i][j][num2] == 1):
                                flag = 1
                            elif L[i][j][num1] == 1 and L[i][j][num2] == 1:
                                count += 1
                                if count == 1:
                                    one_i = i
                                    one_j = j
                                elif count == 2:
                                    two_i = i
                                    two_j = j
                    if count == 2 and flag == 0:
                        for j in range(0, 9):
                            if j == num1 or j == num2:
                                continue
                            L[one_i][one_j][j] = 0
                            L[two_i][two_j][j] = 0
                        matrix[one_i][one_j] = 2
                        matrix[two_i][two_j] = 2

def rulefour(g, K, L, matrix):
    for num1 in range(0, 9):
        for num2 in range(0, 9):
            for num3 in range(0,9):
                if num1 == num2 or num2 == num3 or num3 == num1:
                    continue
                for i in range(0, 9):
                    flag = 0
                    count = 0
                    for j in range(0, 9):
                        if (L[i][j][num1] == 0 and L[i][j][num2] == 0 and L[i][j][num3] == 1) or (L[i][j][num1] == 0 and L[i][j][num2] == 1 and L[i][j][num3] == 0) or (L[i][j][num1] == 1 and L[i][j][num2] == 0 and L[i][j][num3] == 0) or (L[i][j][num1] == 0 and L[i][j][num2] == 1 and L[i][j][num3] == 1) or (L[i][j][num1] == 1 and L[i][j][num2] == 0 and L[i][j][num3] == 1) or (L[i][j][num1] == 1 and L[i][j][num2] == 1 and L[i][j][num3] == 0):
                            flag = 1
                        elif (L[i][j][num1] == 1 and L[i][j][num2] == 1 and L[i][j][num3] == 1):
                            count += 1
                            if count == 1:
                                one_ind = j
                            elif count == 2:
                                two_ind = j
                            elif count == 3:
                                three_ind = j
                    if count == 3 and flag == 0:
                        for j in range(0, 9):
                            if j == num1 or j == num2 or j == num3:
                                continue
                            L[i][one_ind][j] = 0
                            L[i][two_ind][j] = 0
                            L[i][three_ind][j] = 0
                        matrix[i][one_ind] = 3
                        matrix[i][two_ind] = 3
                        matrix[i][three_ind] = 3
            
    for num1 in range(0, 9):
        for num2 in range(0, 9):
            for num3 in range(0,9):
                if num1 == num2 or num2 == num3 or num3 == num1:
                    continue
                for i in range(0, 9):
                    flag = 0
                    count = 0
                    for j in range(0, 9):
                        if (L[j][i][num1] == 0 and L[j][i][num2] == 0 and L[j][i][num3] == 1) or (L[j][i][num1] == 0 and L[j][i][num2] == 1 and L[j][i][num3] == 0) or (L[j][i][num1] == 1 and L[j][i][num2] == 0 and L[j][i][num3] == 0) or (L[j][i][num1] == 0 and L[j][i][num2] == 1 and L[j][i][num3] == 1) or (L[j][i][num1] == 1 and L[j][i][num2] == 0 and L[j][i][num3] == 1) or (L[j][i][num1] == 1 and L[j][i][num2] == 1 and L[j][i][num3] == 0):
                            flag = 1
                        elif (L[j][i][num1] == 1 and L[j][i][num2] == 1 and L[j][i][num3] == 1):
                            count += 1
                            if count == 1:
                                one_ind = j
                            elif count == 2:
                                two_ind = j
                            elif count == 3:
                                three_ind = j
                    if count == 3 and flag == 0:
                        for j in range(0, 9):
                            if j == num1 or j == num2 or j == num3:
                                continue
                            L[one_ind][i][j] = 0
                            L[two_ind][i][j] = 0
                            L[three_ind][i][j] = 0
                        matrix[one_ind][i] = 3
                        matrix[two_ind][i] = 3
                        matrix[three_ind][i] = 3

    for num1 in range(0, 9):
        for num2 in range(0, 9):
            for num3 in range(0,9):
                if num1 == num2 or num2 == num3 or num3 == num1:
                    continue
                for I in range(0, 9, 3):
                    for J in range(0, 9, 3):
                        count = 0
                        flag = 0
                        for i in range(I, I+3):
                            for j in range(J, J+3):
                                if (L[i][j][num1] == 0 and L[i][j][num2] == 0 and L[i][j][num3] == 1) or (L[i][j][num1] == 0 and L[i][j][num2] == 1 and L[i][j][num3] == 0) or (L[i][j][num1] == 1 and L[i][j][num2] == 0 and L[i][j][num3] == 0) or (L[i][j][num1] == 0 and L[i][j][num2] == 1 and L[i][j][num3] == 1) or (L[i][j][num1] == 1 and L[i][j][num2] == 0 and L[i][j][num3] == 1) or (L[i][j][num1] == 1 and L[i][j][num2] == 1 and L[i][j][num3] == 0):
                                    flag = 1
                                elif (L[i][j][num1] == 1 and L[i][j][num2] == 1 and L[i][j][num3] == 1):
                                    count += 1
                                    if count == 1:
                                        one_i = i
                                        one_j = j
                                    elif count == 2:
                                        two_i = i
                                        two_j = j
                                    elif count == 3:
                                        three_i = i
                                        three_j = j
                        if count == 3 and flag == 0:
                            for j in range(0, 9):
                                if j == num1 or j == num2 or j == num3:
                                    continue
                                L[one_i][one_j][j] = 0
                                L[two_i][two_j][j] = 0
                                L[three_i][three_j][j] = 0
                            matrix[one_i][one_j] = 3
                            matrix[two_i][two_j] = 3
                            matrix[three_i][three_j] = 3
                      
   

if __name__ == '__main__':
    pass

f = open("test_sudoku.txt", 'r')
l = f.readlines()
for i in range(0,len(l)):
    l[i]=l[i][:-1]
    l[i] = l[i].split(' ')
    l[i][-1] = l[i][-1][:-1]
    k.append(l[i])
    
graph = {}
for i in range(0, 9):
    for j in range(0, 9):
        node1 = str(i) + str(j)
        for n in range(i+1, 9):
            node2 = str(n) + str(j)
            add_edge(node1, node2)
        for n in range(j+1, 9):
            node2 = str(i) + str(n)
            add_edge(node1, node2)
        x = int(math.floor(float(i/3)) * 3)
        y = int(math.floor(float(j/3)) * 3)
        for f in range(x, x+3):
            for s in range(y, y+3):
                node3 = str(f) + str(s)
                add_edge(node1, node3)
       
mat = [[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9]]
# mat = number of possibilities at each box

ll = [1,1,1,1,1,1,1,1,1]
for i in range(0, len(ll)):
    ll[i] = [1]*9
for i in range(0, len(ll)):
    for j in range(0, len(ll)):
        ll[i][j] = [1]*9
# ll = 3D matrix
#initialising the matrix and  ll.
for i in graph:
    if k[int(i[0])][int(i[1])] != '-':
        mat[int(i[0])][int(i[1])] = 1
        for j in range(0, 9):
            ll[int(i[0])][int(i[1])][j] = 0
        ll[int(i[0])][int(i[1])][int(k[int(i[0])][int(i[1])])-1] = 1
        for v in graph[i]:
            if ll[int(v[0])][int(v[1])][int(k[int(i[0])][int(i[1])])-1] == 1:
                ll[int(v[0])][int(v[1])][int(k[int(i[0])][int(i[1])])-1] = 0
                mat[int(v[0])][int(v[1])] -= 1

print "unsolved sudoku"
for i in k:
    print i
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# rulethree(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)
# ruletwo(graph, k, ll, mat)
# ruleone(graph, k, ll, mat)





countt = 0
while(1):
    countt = countt + 1
    rulethree(graph, k, ll, mat)
    rulefour(graph, k, ll, mat)
    ruletwo(graph, k, ll, mat)
    ruleone(graph, k, ll, mat)
          
    mark = 0
    for i in range(0,9):
        if '-'  in k[i]:
            mark =1
    if mark == 0 :
        print countt
        break;
    if countt == 15:
        break
print
print

print "solved sudoku"
for i in k:
    print i
#print mat
#print ll
