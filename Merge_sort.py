def merge(l1,s,m,e):
    i = s
    j = m + 1
    ans = []
    while(i<=m and j<=e):
        if (l1[i]<l1[j]):
            ans.append(l1[i])
            i +=1
        elif(l1[i] > l1[j]):
            ans.append(l1[j])
            j += 1
        elif (l1[i]==l1[j]):
            ans.append(l1[i])
            ans.append(l1[j])
            i += 1
            j += 1
    while (i<=m):
        ans.append(l1[i])
        i +=1
    while (j<=e):
        ans.append(l1[j])
        j +=1 
    startofmyans = 0
    startofmylist = s
    while(startofmylist<=e):
        l1[startofmylist]=ans[startofmyans]
        startofmyans +=1
        startofmylist +=1
    return
def mergesorthelper(l1,s,e):
    if (s>=e):
        return
    m = s +(e-s)//2
    mergesorthelper(l1,s,m)
    mergesorthelper(l1,m+1,e)
    merge(l1,s,m,e)  
    return
def mergesort(l1):
    return mergesorthelper(l1,0,len(l1)-1)
l1 = [6,5,12,10,9,1]  
mergesort(l1)
print(l1)  