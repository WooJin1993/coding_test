from operator import itemgetter

def solution(k, num, links):
    result = []
    threshold = (sum(num) // k) + 1
    
    while k > 0:
        idx_list = []
        idx = links.index([-1, -1])
        links[idx] = [-1]
        idx_list.append(idx)
        group_sum = 0
        group_sum += num[idx]
        
        while sum(itemgetter(*idx_list)(num)) < threshold:
            # 자식
            for link in links:
                node = [l for l in link if l not in idx_list and l != -1] 
                if not node:
                    if group_sum + num[node[0]] < threshold:
                        idx_list.append(node[0])
                        group_sum += num[node[0]]
                    else:
                        result.append(group_sum)
                        k -= 1
                        break
            # 부모
            for i, link in enumerate(links):
                if idx_list[-1] in link:
                    idx_list.append(i)
                    link[i][link[i].index(idx_list[-1])] = -1
                if sum(itemgetter(*idx_list)(num)) < threshold:
                    idx_list.append()
        
        for idx in idx_list:
            for link in links:
                if idx in link:
                    link[link.index(idx)] = -1
        
        k -= 1
        result.append(sum(itemgetter(*idx_list)(num)))
    
    return max(result)