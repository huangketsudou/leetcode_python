from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math

class Solution:
    #leetcode-282,
    # https://leetcode-cn.com/problems/expression-add-operators/solution/gei-biao-da-shi-tian-jia-yun-suan-fu-by-leetcode/
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            if index == N:

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:

                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:

                # SUBTRACTION
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])
        return answers

class Solution2:
    #powcai
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        # 参数列表， 位置， 之前输出， 之前综合， 前一个数
        def helper(index, preOutStr, preSum, preValue):
            if index == len(num):
                if preSum == target:
                    res.append(preOutStr)
                return
            # 后面的数都做乘法, 还小于前面总和
            if max(1, abs(preValue)) * (int(num[index:])) < abs(target - preSum):#剪纸
                return
            for i in range(index, index + 1 if num[index] == '0' else len(num)):
                cur = num[index:i + 1]
                curValue = int(cur)
                if not preOutStr:#保证前面有数
                    helper(i + 1, cur, curValue, curValue)
                else:
                    helper(i + 1, preOutStr + '+' + cur, preSum + curValue, curValue)
                    helper(i + 1, preOutStr + '-' + cur, preSum - curValue, -curValue)
                    helper(i + 1, preOutStr + '*' + cur, preSum - preValue + curValue * preValue, curValue * preValue)
        helper(0, '', 0, 0)
        return res

