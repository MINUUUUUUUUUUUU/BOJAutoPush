class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        answer = ""
        for i in range(len(strs[0])):
            flag = 0
            for str in strs:
                if len(str) <= i or str[i] != strs[0][i]:
                    flag = 1

            if flag == 0:
                answer += strs[0][i]
            elif flag == 1:
                break

        return answer