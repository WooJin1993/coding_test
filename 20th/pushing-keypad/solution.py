# 문제: https://programmers.co.kr/learn/courses/30/lessons/64061

def get_dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    return abs(x1 - x2) + abs(y1 - y2)

def solution(numbers, hand):
    key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                0: (3, 1)}
    left_pos, right_pos = (3, 0), (3, 2)
    answer = ""
    
    for num in numbers:
        next_pos = key_dict[num]
        
        if num in [1, 4, 7]:
            answer += "L"
            left_pos = next_pos
        elif num in [3, 6, 9]:
            answer += "R"
            right_pos = next_pos
        else:
            if hand == "left":
                if get_dist(next_pos, left_pos) <= get_dist(next_pos, right_pos):
                    answer += "L"
                    left_pos = next_pos
                else:
                    answer += "R"
                    right_pos = next_pos
            else:
                if get_dist(next_pos, right_pos) <= get_dist(next_pos, left_pos):
                    answer += "R"
                    right_pos = next_pos
                else:
                    answer += "L"
                    left_pos = next_pos
    
    return answer