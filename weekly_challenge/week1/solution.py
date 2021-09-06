def solution(price, money, count):
    total_price = price * count * (count+1)//2
    
    if total_price <= money:
        return 0
    else:
        return total_price - money