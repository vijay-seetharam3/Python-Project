def sublists(lst,k):
    n = len(lst)
    for start in range(n):
		for end in range(start + 1, n + 1):
		    if sum(lst[start:end])==k:
			    print(max(lst[start:end]),min(lst[start:end]))
original_list = list(map(int,input().split()))
sublists(original_list[:-1],original_list[-1])