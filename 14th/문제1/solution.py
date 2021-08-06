def solution(s):
    num_dict = dict()
    num_dict["zero"] = "0"	
    num_dict["one"] = "1"	
    num_dict["two"] = "2"	
    num_dict["three"] = "3"	
    num_dict["four"] = "4"	
    num_dict["five"] = "5"	
    num_dict["six"] = "6"	
    num_dict["seven"] = "7"	
    num_dict["eight"] = "8"	
    num_dict["nine"] = "9"
    
    for key, value in num_dict.items():
        s = s.replace(key, value)
        
    return int(s)