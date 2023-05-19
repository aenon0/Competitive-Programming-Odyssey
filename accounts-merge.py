class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        size = [1] * len(accounts)
        email = {}
        
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(owner1, owner2):
            rep1 = find(owner1)
            rep2 = find(owner2)
            if rep1 == rep2:
                return
            
            if size[rep2 ] > size[rep1]:
                rep1,rep2 = rep2,rep1
            
            parent[rep2] = rep1
            size[rep1] += size[rep2]
            return
        
        for owner in range(len(accounts)):
            for indx in range(1, len(accounts[owner])):
                e = accounts[owner][indx]
                if e not in email:
                    email[e] = owner
                else:
                    union(owner, email[e])
        
        ans_dict = defaultdict(list)
        for key in sorted(email.keys()):
            # print("K: ",key)
            ans_dict[find(email[key])].append(key)
            
        # print(ans_dict)
        ans = [ ]
        for key in ans_dict.keys():
            temp = [accounts[key][0]]
            temp.extend(ans_dict[key])
            ans.append(temp)
        return ans
          # return [ ]
            
        
            
            
        
                                        
            
        
#         belongs = defaultdict(lambda: -1)
#         acc_dict = defaultdict(int)
#         sizes = defaultdict(set)
#         for node in range(len(accounts)):
#             sizes[node] = set(accounts[node][1 : ]) 
#             acc_dict[node] = node
            
#         def find(node):
#             return acc_dict[node]
        
#         def union(node1, node2):
#             rep1 = find(node1)
#             rep2 = find(node2)
            
#             size1 = len(sizes[rep1])
#             size2 = len(sizes[rep2])
#             check = True if size1 > size2 else False
#             if rep1 != rep2:
#                 for node in range(len(accounts)):
#                     if check and belongs[node] == rep2:
#                         _union = sizes[rep1].union(sizes[node])
#                         sizes[rep1] = _union
#                         acc_dict[node] = rep1
                        
#                     if not check and belongs[node] == rep1:
#                         _union = sizes[rep2].union(sizes[node])
#                         sizes[rep2] = _union
#                         acc_dict[node] = rep2
                
#         for indx in range(len(accounts)):
#             for i in range(1, len(accounts[indx])):
                
#                 if belongs[accounts[indx][i]] == -1:
#                     belongs[accounts[indx][i]] = indx
#                 else:
#                     # print(accounts[indx], belongs[accounts[indx][i]])
#                     curr_email = 
#                     if acc_dict[indx] == indx and acc_dict[belongs[accounts[indx][i]]] == belongs[accounts[indx][i]]:
#                         size1 = len(sizes[indx])
#                         size2 = len(sizes[belongs[accounts[indx][i]]])
#                         check = True if size1 > size2 else False
#                         _union = sizes[indx].union(sizes[belongs[accounts[indx][i]]])
#                         if check:
#                             sizes[indx] = _union
#                             acc_dict[belongs[accounts[indx][i]]] = indx

#                         else:
#                             sizes[belongs[accounts[indx][i]]] = _union
#                             acc_dict[indx] = belongs[accounts[indx][i]]
#                     union(indx, belongs[accounts[indx][i]])
                    
#         ans = [ ] 
#         visited_rep = set()
#         for key in acc_dict.keys():
            
#             if acc_dict[key] in visited_rep:
#                 continue
#             visited_rep.add(acc_dict[key])
#             temp = [accounts[acc_dict[key]][0]]
#             temp.extend(sorted(sizes[acc_dict[key]]))
#             ans.append(copy.deepcopy(temp))
            
#         return ans