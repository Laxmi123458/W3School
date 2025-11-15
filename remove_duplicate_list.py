lists=[1,3,3,1,5,7,8,9]
removed_duplicate_list= []
for x in lists:
    if x in removed_duplicate_list:
        continue
    else:
        removed_duplicate_list.append(x)
print(removed_duplicate_list)