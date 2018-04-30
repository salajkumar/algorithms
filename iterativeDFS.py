# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 09:38:28 2018

@author: salaj 875715
working version ~ 20 seconds
"""
import time
def buildRevGraph():
    
    i = 0

    g = {}
    g_rev = {}
    
    start = time.time()
        
    for name in range (1, 875715):
        g[str(name)] = [0]
        g_rev[str(name)] = [0]
    
    end = time.time()
    
    print(name, 'nodes created in', (end - start), 'seconds')
    
    in_file = open('SCC.txt', 'r')
    
    start = time.time()
    
    for line in in_file:
        src = line.split()[0]
        dest = line.split()[1]
        
        g[src].append(dest)
        g_rev[dest].append(src)
        i += 1
    
    end = time.time()
    
    in_file.close()
    
    print(i, 'edges added', 'in', (end - start), 'seconds')
    
    return g, g_rev

f_value = []


def DFS_Loop(g):

    stack = []
    # iterate over the list of nodes
    for node in g.keys():

        if g[node][0] == 0:
            stack.append(node)

        while len(stack)> 0:
            
            if g[stack[-1]][0] == 0:
            
                g[stack[-1]][0] = 1
                children = g[stack[-1]][1:]
                
                if len(children) == 0:
                    f_value.append(stack.pop())     # sink node
                else:
                    t = 0
                    for child in reversed(children):
                        if g[child][0] == 0:
                            stack.append(child)
                            g[child][0] = 1
                            t += 1
                    if t == 0:
                        f_value.append(stack.pop()) # all children visited
            else:
                children = g[stack[-1]][1:]
                
                if len(children) == 0:
                    f_value.append(stack.pop())     # sink node
                else:
                    t = 0
                    for child in reversed(children):
                        if g[child][0] == 0:
                            stack.append(child)
                            g[child][0] = 1
                            t += 1
                    if t == 0:
                        f_value.append(stack.pop())

def SCC_Loop(g):

    result = [0,0,0,0,0]
    stack = []
    SCC = 0
    # iterate over the list of nodes
    for node in reversed(f_value):
        if SCC > min(result):
            result.append(SCC)
            result.remove(min(result))
        SCC = 0
        if g[node][0] == 0:
            stack.append(node)
            SCC += 1

        while len(stack)> 0:
            
            if g[stack[-1]][0] == 0:
            
                g[stack[-1]][0] = 1
                children = g[stack[-1]][1:]
                
                if len(children) == 0:
                    stack.pop()
                else:
                    t = 0
                    for child in children:
                        if g[child][0] == 0:
                            stack.append(child)
                            g[child][0] = 1
                            SCC += 1
                            t += 1
                    if t == 0:
                        stack.pop()
            else:
                
                children = g[stack[-1]][1:]

                if len(children) == 0:
                    stack.pop()
                    
                else:
                    t = 0
                    for child in children:
                        if g[child][0] == 0:
                            stack.append(child)
                            g[child][0] = 1
                            SCC += 1
                            t += 1
                    if t == 0:
                        stack.pop()
        
    return result

start = time.time()                

g, g_rev = buildRevGraph()
DFS_Loop(g_rev)
del g_rev
result = SCC_Loop(g)
end = time.time()

print('done in ', end - start, 'seconds')
print(sorted(result, reverse = True))