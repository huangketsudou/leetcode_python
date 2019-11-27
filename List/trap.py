from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<3:
            return 0
        left,right=0,n-1
        answer=0
        leftmax=rightmax=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    answer+=(leftmax-height[left])
                left+=1
            else:
                if height[right]>=rightmax:
                    rightmax=height[right]
                else:
                    answer+=(rightmax-height[right])
                right-=1
        return answer


class Solution2:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<3:return 0
        answer=0
        leftmax=[0]*n
        rightmax=[0]*n
        #最右边有无限高的强，因此中间的装水受限于左边的大小
        leftmax[0]=height[0]
        for i in range(1,n):
            leftmax[i]=max(height[i],leftmax[i-1])
        rightmax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightmax[i]=max(height[i],height[i+1])
        for i in range(1,n-1):
            answer+=min(leftmax[i],rightmax[i])-height[i]
        return answer



class Solution3:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n<3:return 0
        answer=current=0
        #这个栈维护一个递减的数组，当发现数组值不单调增时出栈
        st=[]
        while current<n:
            while len(st)!=0 and height[current]>height[st[-1]]:
                top=st.pop(-1)
                if len(st)==0:
                    break
                #横向计算可接水长度
                distance=current-st[-1]-1
                boundedheight=min(height[current],height[st[-1]])-height[top]
                answer+=distance*boundedheight
            st.append(current)
            current+=1


        return answer


k=Solution3()
print(k.trap([5,4,0,1]))
