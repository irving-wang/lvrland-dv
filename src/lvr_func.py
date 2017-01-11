from numpy import isnan

def remove_outlier(df, bottom, top):
    print('type = ',type(df))
    result = []
    for v in df:
        if isnan(v) or v > top or v < bottom:
            continue
        result.append(v)
    return result

def outlier_count_over(df, top):
    count = 0
    for v in df:
        if(v<top):
            count += 1
    return count

def count_keys(data):
    dic = {}
    for v in data:
        if v in dic:
            dic[v] += 1
        else:
            dic[v] = 1
    return dic

def calcount(data):
    c = 0
    for v in data:
        if isnan(v):
            continue
        c += 1
    return c

def calrange(data, bottom, top):
    c = 0
    for v in data:
        if not isnan(v):
            if v >= bottom and v < top:
                c +=1
    return c

def calsum(data):
    res = 0.0
    for v in data:
        if isnan(v):
            continue
        res += v
    return res

def calaverage(data):
    c = 0
    res = 0.0
    for v in data:
        if isnan(v):
            continue
        c += 1
        res += v
    return res/c

ping = 0.3025

def calaverage_ping(data):
    return calaverage(data)/ping

def funcpass():
    pass
