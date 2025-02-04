class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        inc = True
        count = 0
        for i in range(l - 1):
            sub = []
            if nums[i] > nums[i + 1]:
                inc = False
            elif nums[i] < nums[i + 1]:
                inc = True
            else:
                continue
            for j in range(i, l-1):
                #print(nums[j])
                sub.append(nums[j])
                if j == l-2:
                    if inc and nums[l-1] > nums[l-2]:
                        sub.append(nums[j])
                    if not inc and nums[l-1] < nums[l-2]:
                        sub.append(nums[j])
                    else:
                        break
                if inc:
                    if nums[j + 1] > nums[j]:
                        print("YES")
                        continue
                    else:
                        break
                elif not inc:
                    if nums[j + 1] < nums[j]:
                        continue
                    else:
                        break
                if nums[j+1] == nums[j]:
                    break
            print(sub)
            if len(sub) > count:
                count = len(sub)

        if count == 0:
            count = 1
            
        return count

            
        