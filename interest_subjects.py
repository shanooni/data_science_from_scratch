from collections import Counter,defaultdict
from data import users,interests

def common_interest(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]
    
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
# print(user_ids_by_interest)

interest_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)
# print(interest_by_user_id)

def most_common_interest_with(user):
    return Counter(interested_user_id
                   for interest in interest_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"]) 
    
# print(most_common_interest_with(users[0]))

words_and_count = Counter(word 
    for user,interest in interests
    for word in interest.lower().split()
)

for word,count in words_and_count.most_common():
    if count > 1:
        print(f"word : {word} \n count: {count}")