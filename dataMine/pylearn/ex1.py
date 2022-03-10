def txt_to_list(path):
    file=open(path)    
    dataMat=[]  
    for line in file.readlines():    
        curLine=line.strip().split("  ") 
        dataMat.append(curLine)
    return dataMat

def hello():
    print("hello")
    
def load_data_set():
    data_set = txt_to_list("dataMine\data.txt")
    # data_set = [['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'],
    #         ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'],
    #         ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]
    return data_set


def create_C1(data_set):
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1


def is_apriori(Ck_item, Lksub1):
    print("ckitem",Ck_item)
    print("lksub1",Lksub1)
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True


def create_Ck(Lksub1, k):
    print(Lksub1)
    Ck = set()
    len_Lksub1 = len(Lksub1)
    print(len_Lksub1)
    list_Lksub1 = list(Lksub1)
    print(list_Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:
                Ck_item = list_Lksub1[i] | list_Lksub1[j]
                # pruning
                if is_apriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    return Ck


def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):
    Lk = set()
    item_count = {}
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk


def generate_L(data_set, k, min_support):
    support_data = {}
    C1 = create_C1(data_set)
    L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(2, k+1):
        Ci = create_Ck(Lksub1, i)
        Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data

if __name__ == "__main__":
    data_set = load_data_set()
    L, support_data = generate_L(data_set, k=3, min_support=0.15)
    for Lk in L:
        print ("="*50)
        print ("frequent " + str(len(list(Lk)[0])) + "-itemsets\t\tsupport")
        print ("="*50)
        for freq_set in Lk:
            print (freq_set, support_data[freq_set])