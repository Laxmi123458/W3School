"""
Simple Array Rotation

Input: [1,2,3,4,5], rotate by 2 → Output: [4,5,1,2,3]
Focus: List slicing and indexing.
"""

list= [1,2,3,4,5]

for i in range(1,len(list),2):
    k=2
    print(list[ :k])
