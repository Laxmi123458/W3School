inputs=[1, 2, 2, 3, 3, 3]
new_refined_input=[]
for i in inputs:
    if i in new_refined_input:
        continue
    else:
        new_refined_input.append(i)
print(new_refined_input)