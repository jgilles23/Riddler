#Riddler 538 by jgilles
#https://fivethirtyeight.com/features/can-you-win-riddler-jenga/
#2/19/2021
#Python code

#Import the problem
rows = [280,168,162,360,60,256,126]
columns = [183708,245760,117600]

def getThirds(x):
    #Setup set to hold the results
    mixes = set()
    #Iterate through the 3 possible digits
    for a in range(1,10):
        if (x/a)%1 != 0: continue
        for b in range(a,10):
            if (x/a/b)%1 != 0: continue
            for c in range(b,10):
                if a*b*c != x: continue
                mixes.add((a,b,c))
                mixes.add((a,c,b))
                mixes.add((b,a,c))
                mixes.add((b,c,a))
                mixes.add((c,a,b))
                mixes.add((c,b,a))
    return mixes

row_mixes = [getThirds(x) for x in rows]

def iterate_mixes(row, col_remainders):
    if row == len(row_mixes):
        return tuple()
    for mix in row_mixes[row]:
        new_remainders = [rem/x for x,rem in zip(mix, col_remainders)]
        if all([(x%1)==0 for x in new_remainders]): #Check all remainders are zero
            q = iterate_mixes(row+1,new_remainders)
            if q is not None:   
                answer = [mix]
                answer.extend(q)
                #print(q)
                return answer
    #The find was a failure
    return None

print(len(row_mixes))
ans_sets = iterate_mixes(0,columns)
ans = [100*a+10*b+c for a,b,c in ans_sets]
print("ans",ans)

def mul_list(L):
    x = 1
    for y in L:
        x *= y
    return x

new_rows = [mul_list(x) for x in ans_sets]
new_cols = [mul_list(x) for x in zip(*ans_sets)]

print('old rows',rows,'columns',columns)
print('new rows',new_rows,'columns',new_cols)