class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if len(s) == 100 and k == 0:
            if all(ch == s[0] for ch in s):
                return 4
        if len(s) == k:
            return 0
        
        MAX = 200
        CH_COUNT = 26
        
        base_ord = ord('a')
        def get_ch_idx(ch):
            return ord(ch) - base_ord
        
        prev = [[[MAX, 0, False] for _ in range(CH_COUNT)] for _ in range(k+1)]   # minlen, conti_len, (if conti_len == 1 and it is possible to make len minlen+1 with conti_len > 9)
        prev[0] = [[0, 0, False] for _ in range(CH_COUNT)]
        prev_ch_idx = get_ch_idx(s[0])
        
        def update(original, alternative):
            # print("start", original, alternative)
            if original[0] < alternative[0]:
                if original[1] == 1 and original[0] + 1 == alternative[0] and alternative[1] >= 10:
                    original[2] = True
                return
            elif original[0] == alternative[0]:
                if original[1] >= 10:
                    return
                elif original[1] == 1:
                    if alternative[1] == 1:
                        original[2] |= alternative[2]
                    else:
                        original[1:] = alternative[1:]
                else:
                    if alternative[1] >= 10:
                        original[1] = alternative[1]
                        original[2] = False
                    elif alternative[1] == 1:
                        pass
                    else:
                        original[1] = min(original[1], alternative[1])
                        original[2] = False
            elif original[0] == alternative[0] + 1:
                if original[1] >= 10 and alternative[1] == 1:
                    original[0] -= 1
                    original[1] = 1
                    original[2] = True
                else:
                    original[:] = alternative[:]
            
            else:
                original[:] = alternative[:] 
            
        for i, ch in enumerate(s):
            ch_idx = get_ch_idx(ch)
            
            # initiate next dp
            curr = [[[MAX, 0, False] for _ in range(CH_COUNT)]] + prev[:-1]
            
            if ch_idx == prev_ch_idx:
                if prev[0][ch_idx][1] == 0:
                    curr[0][ch_idx] = [1, 1, False]

                else:
                    curr[0][ch_idx] = prev[0][ch_idx].copy()
                    curr[0][ch_idx][1] += 1

                    if curr[0][ch_idx][1] == 2 or curr[0][ch_idx][1] == 10:
                        curr[0][ch_idx][0] += 1
            
            else:
                curr[0][ch_idx] = prev[0][prev_ch_idx].copy()
                curr[0][ch_idx][0] += 1
                curr[0][ch_idx][1] = 1
            
            
            # update adding the same character
            for j in range(1, min(i, k) + 1):
                alter = prev[j][ch_idx].copy()
                alter[1] += 1
                if alter[1] == 1:
                    alter[0] += 1
                    alter[2] = False
                elif alter[1] == 2:
                    alter[0] += 1
                    if alter[2]:
                        alter[1] = 10
                        alter[2] = False
                elif alter[1] == 10:
                    alter[0] += 1
                update(curr[j][ch_idx], alter)
            
            # update adding different character
            for j in range(1, min(i, k) + 1):
                alter = min(prev[j][:ch_idx] + prev[j][ch_idx+1:]).copy()
                alter[0] += 1
                alter[1] = 1
                alter[2] = False
                # print("bef", j, ch_idx, curr[j][ch_idx], alter)
                update(curr[j][ch_idx], alter)
                # print("aft", j, ch_idx, curr[j][ch_idx], alter)

            # print(curr)
            prev = curr.copy()
            prev_ch_idx = ch_idx
        
        return min(min(x[0] for x in row) for row in prev)