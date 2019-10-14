class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        m,n=len(nums1),len(nums2)
        if m>n:#保证i计算出的j一定落在可取的范围内
            nums1,nums2,m,n=nums2,nums1,n,m
        if n==0:#证明两个都为空
            return 0
        imin,imax,half=0,m,(m+n+1)//2
        while imin<=imax:
            i=(imin+imax)//2
            j=half-i
            if i<m and nums2[j-1]>nums1[i]:
                imin=i+1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            else:
                if i==0:#nums1的最小值大于nums2的最大值
                    maxleft=nums2[j-1]
                elif j==0:#m==n时，成立
                    maxleft=nums1[i-1]
                else:
                    maxleft=max(nums1[i-1],nums2[j-1])

                if (m+n)%2==1:
                    return maxleft

                if i==m:#nums1的最大值小于nums2的最小值
                    minright=nums2[j]
                elif j==n:#m==n时成立
                    minright=nums1[i]
                else:
                    minright=min(nums1[i],nums2[j])

                return (maxleft+minright)/2.0



k=Solution()
print(k.findMedianSortedArrays([1,3],[]))
