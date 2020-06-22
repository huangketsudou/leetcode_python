class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == "a")
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)
        if not value:  # 字符串为空时，只有a可以为空，b不能为空，所以不能存在b字符，这里就包含了pattern和value都为空的情况
            return count_b == 0
        if not pattern:  # pattern为空，而value不为空，必定不能匹配
            return False
        for len_a in range(len(value) // count_a + 1):  # a字符的可能长度
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):  # b的构成是有意义的
                len_b = 0 if count_b == 0 else rest // count_b
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:  # 分配字符串
                            value_a = sub
                        elif value_a != sub:  # 已被分配字符串，但是不相等
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]  # 同ch=='a'的情况
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False
