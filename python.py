def longestCommonSubstring(string_1, string_2):
    len_1 = len(string_1)
    len_2 = len(string_2)
    
    LongestCommonSubstring = [[0 for i in range(len_2 + 1)] for j in range(len_1 + 1)]
    
    res = 0
    
    for i in range(len_1 + 1):
        for j in range(len_2 + 1):
            if (i == 0 or j == 0):
                LongestCommonSubstring[i][j] = 0
            elif (string_1[i-1] == string_2[j-1]):
                LongestCommonSubstring[i][j] = LongestCommonSubstring[i-1][j-1] + 1
                res = max(res, LongestCommonSubstring[i][j])
                print(LongestCommonSubstring)
            else:
                LongestCommonSubstring[i][j] = 0
    return res 
    
    
string_1 = input("enter string 1:")
string_2 = input("enter string 2:")

if (string_1 and string_2):
    print(f'Lenght of longest common substring is:{longestCommonSubstring(string_1, string_2)}')
else:
    print(f'Enter a valid string')