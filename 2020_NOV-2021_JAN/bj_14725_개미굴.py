# 출력: 개미굴의 시각화된 구조

# 체크할 조건
# 같은 층에 여러 방이 있는 경우 사전 순서대로 나온다.
# 하나의 로봇 개미는 끝까지 간다.

# 트리를 만든 후에 DFS로 출력한다.

# 트리는 list로 만들고, 각 요소는 노드로 dict에 저장한다.
# 각 노드는 (가리키는 요소, 루트)를 값으로 가진다.
# 루트가 다르면 다른 트리에 있는 것으로 본다.

# def trav(tree, key, s, dashs, root):
#     print(dashs + key)
#     if tree[s][key]:
#         for e, r in tree[s][key]:
#             if r == root: trav(tree, e, s+1, dashs + '--', root)

# def solution(N):
#     tree = []
#     id = 1
#     for i in range(N):
#         inp = list(input().split())
#         k, info = int(inp[0]), inp[1:]
#         info.append(None)
        
#         root = info[0]
#         for j in range(len(info) - 1):
#             if len(tree) == j:
#                 tree.append(dict())
#             if tree[j].get(info[j]):
#                 if not info[j+1]: break
#                 tree[j][info[j]].append((info[j+1], root))
#             else:
#                 if not info[j+1]: 
#                     tree[j][info[j]] = None
#                     break
#                 tree[j][info[j]] = [(info[j+1], root)]
    
#     for _ in range(len(tree)):
#         for key in tree[_].keys():
#             if tree[_][key]: tree[_][key].sort()
    
#     for key in sorted(tree[0].keys()):
#         trav(tree, key, 0, '', key)

# if __name__ == '__main__':
#     solution(int(input()))


# dict를 하나의 노드로 만든다.
# 각 노드 구성 > 부모노드이름 : {자식노드이름: 자식노드들dict()}
# apple: {apple: {}}, banana: {kiwi: {}}}

def trav(tree, key, dashs):
    child = tree.get(key)
    if child:
        for k in sorted(child.keys()):
            print(dashs + k)
            if child.get(k):
                trav(child, k, dashs + '--')

def solution(N):
    tree = dict()
    for _ in range(N):
        inp = list(input().split())
        k, data = int(inp[0]), inp[1:]

        if not data[0] in tree: tree[data[0]] = dict()
        temp = tree
        for i in range(1, len(data)):
            children = temp.get(data[i-1])
            if children and (data[i] in children):
                temp = children
                continue
            children[data[i]] = dict()
            temp = children
    
    for key in sorted(tree.keys()):
        print(key)
        trav(tree, key, '--')

if __name__ == '__main__':
    solution(int(input()))