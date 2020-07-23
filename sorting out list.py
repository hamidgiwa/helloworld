#To sort one list by using values of a different list
first_list =["0","X","A","C","D","K"]
Second_list =["1","2","3","4""5""6"]
Zipped_pairs = zip(first_list,Second_list)
sorted_pairs = sorted(Zipped_pairs)
result =[item[1] for item in sorted_pairs]
print(result)