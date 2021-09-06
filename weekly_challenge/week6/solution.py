def solution(weights, head2head):
    n = len(weights)
    boxers = []
    
    for i in range(n):
        win = 0
        heavy_win = 0
        total = n
        
        for j in range(n):
            if head2head[i][j] == "N":
                total -= 1
                continue
            
            if head2head[i][j] == "W":
                win += 1
                
                if weights[i] < weights[j]:
                    heavy_win += 1
                    
        try:
            win_rate = win / total
        except ZeroDivisionError:
            win_rate = 0
        
        boxers.append((win_rate, heavy_win, weights[i], i + 1))
    
    return [boxer[3] for boxer in sorted(boxers, key=lambda x: (-x[0], -x[1], -x[2], x[3]))] 