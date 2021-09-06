from collections import defaultdict

def solution(table, languages, preference):
    table_dict = dict()
    
    for t in table:
        column = t.split()
        job, langs = column[0], column[1:]
        table_dict[job] = defaultdict(int)
        
        for point, lang in zip(range(1, 6)[::-1], langs):
            table_dict[job][lang] = point
    
    result = defaultdict(int)
    
    for key, value in table_dict.items():
        for lang, pref in zip(languages, preference):
            result[key] += value[lang] * pref
    
    result = list(result.items())
    result.sort(key=lambda x: (-x[1], x[0]))
    
    return result[0][0]