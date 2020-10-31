# 소셜미디어 친구 추천

from collections import defaultdict
def solution(friends, user_id):
    mutual = []
    d = defaultdict(set)

    for friend in friends:
        a, b = friend
        d[a].add(b)
        d[b].add(a)
    
    
    user_friends = d[user_id]

    for user in d.keys():
        if user in user_friends: continue
        if user == user_id: continue

        mutual.append((len(user_friends & d[user]), user))
    
    mutual.sort(reverse = True)
    # print(mutual)

    ans = []
    M = mutual[0][0]
    # print(M)

    for i in range(len(mutual)):
        if M == mutual[i][0]:
            ans.append(mutual[i][1])
        else: break

    return sorted(ans)


print(solution([['david','frank'], ['demi', 'david'], ['frank', 'james'], ['demi', 'james'], ['claire', 'frank']], 'david'))
print(solution([['david','demi'], ['frank', 'demi'], ['demi', 'james']], 'frank'))
# print(solution())