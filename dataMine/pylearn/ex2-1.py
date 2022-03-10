def load_data():
    file=open("dataMine\data.txt")    
    dataMat=[]  
    for line in file.readlines():    
        curLine=line.strip().split("  ") 
        dataMat.append(curLine)
    return dataMat

def create_C1(data_set):
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)   
    return C1

def creat_lk_by_ck(data,lk,min_support,support_data):
    item_count={}
    Lk = set()
    for t in data:
        for item in lk:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk
def create_L(data,k,min_support):
    support_data = {}
    L=[]
    c1=create_C1(data)
    l1=creat_lk_by_ck(data,c1,min_support,support_data)
    lp = l1.copy()
    L.append(lp)
    for i in range(2,k+1):
        Ci = create_Ck(lp,i)
        Li = creat_lk_by_ck(data,Ci,min_support,support_data)
        lp = Li.copy()
        L.append(lp)
    return L,support_data

def apriori(Ck_item, lp):
    for item in Ck_item:
        sub = Ck_item - frozenset([item])
        if sub not in lp:
            return False
    return True

def create_Ck(lp, k):
    Ck = set()
    len_lp = len(lp)
    list_lp = list(lp)
    for i in range(len_lp):
        for j in range(1, len_lp):
            l1 = list(list_lp[i])
            l2 = list(list_lp[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:
                Ck_item = list_lp[i] | list_lp[j]
                # pruning
                if apriori(Ck_item, lp):
                    Ck.add(Ck_item)
    return Ck

def delete_l(data,l):
    for item in data:
        item=item&l
    return data
if __name__ == "__main__":
    #data = load_data()
    data = [['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'],
            ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'],
            ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]

    c1=create_C1(data)
    support_data = {}
    l1=creat_lk_by_ck(data,c1,0.3,support_data)
   # L, support_data = create_L(data, k=3, min_support=0.3)
    c1 =delete_l(c1,l1)
    print(c1)
    print(l1)
    support_data = sorted(support_data.items(),key = lambda s:(s[1],s[0]),reverse=True)
    print(support_data)

    # for Lk in L:
    #     print ("frequent " + str(len(list(Lk)[0])) + "-itemsets\t\tsupport")
    #     for freq_set in Lk:
    #         print (freq_set, support_data[freq_set])
