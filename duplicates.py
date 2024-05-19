nums = [0,0,1,1,1,2,2,3,3,4]

def foo(nums) -> int:
    k = 1 # length of uniques
    haha = False
    length = int(len(nums)-1)
    for i in range(length) :
        if nums[i] == nums[i+1] or nums[i] > nums[i+1]: #if two consecutive numbers are =
            for j in range(int(len(nums))):
                if nums[j]>nums[i]:
                    nums[i+1]=nums[j]
                    break
                if j == length :
                     haha = True  
        if haha == True :
             break
        if nums[i]<nums[i+1] :
                k+=1
    return k
print("k = " + str(foo(nums)))
for i in range(len(nums)) :
    print(str(nums[i]))