def solution(A, K, L):
    if len(A) < (K + L):
        return -1
    else:
        List_Max_K = []
#create a list of max K
        for i in range(0,(len(A)-K+1)):
            sum_val_K = 0
            for j in range(i,i+K):
                sum_val_K += A[j]
            List_Max_K.append(sum_val_K)
        print("List_Max_K",List_Max_K)
#create a list of max L
        List_Max_L = []
        for x in range(0,(len(A)-L+1)):
            sum_val_L = 0
            for y in range(x,x+L):
                sum_val_L += A[y]
            List_Max_L.append(sum_val_L)
        print("List_Max_L",List_Max_L)
#get maximum value and index from max list k and max list L
        max_value_K = max(List_Max_K)
        max_value_L = max(List_Max_L)
        max_index_K = List_Max_K.index(max_value_K)
        max_index_L = List_Max_L.index(max_value_L)
#compare the max value and print result
        if max_value_K >= max_value_L:
            del List_Max_L[max_index_K:K]
            max_value_L = max(List_Max_L)
        else:
            del List_Max_K[max_index_L:L]
            max_value_K = max(List_Max_K)
        total_max = max_value_K + max_value_L
        return total_max
A = [6,13,2,45,7,9,10,56]
K = 3
L = 2
print(solution(A,K,L))
