class Solution:
    def lengthOfLongestSubstring(self, s):
        i = 0
        count = 1
        bestcount = 1
        starti = 0
        while i < len(s):
            if(i+1 == len(s)):
                print('the longest substring is', bestcount)
                break
            if(s[i+1] != s[i]):
                count += 1
            else:
                print('same letters at index', i, 'and index', i+1)
                if(count > bestcount):
                    bestcount = count
                    print('changing starti index to', i)
                    count = 1
                    i=starti 
            i += 1
            starti+=1


Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10

#    for i,letter in enumerate(s):
#        print(i,letter)
