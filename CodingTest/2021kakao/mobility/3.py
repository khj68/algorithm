# 카드 단어 조합 가능한지 찾기

from collections import Counter
def solution(card, word):
    ans = []

    for w in word:
        counter = Counter(w)
        isHere = False
        row_check = [False]*3
        for key, val in counter.items():
            isHereRow = False
            for i, r in enumerate(card):
                if (key in r and val <= r.count(key)):
                    # print(w, key, r, val, r.count(key))
                    isHere = True
                    isHereRow = True
                    row_check[i] = True
            if isHereRow == False: 
                isHere = False
                break
            if isHere == False: break
        if isHere and all(row_check):
            ans.append(w)

    if len(ans) == 0:
        return ['-1']
    return ans


print(solution(['ABACDEFG', 'NOPQRSTU', 'HIJKLKMM'], ['GPQM', 'GPMZ', 'EFU', 'MMNA']))
print(solution(['AABBCCDD', 'KKKKJJJJ', 'MOMOMOMO'], ['AAAKKKKKMMMMM','ABCDKJ']	))