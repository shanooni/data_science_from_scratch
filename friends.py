from collections import Counter
from data import users,friendships

for user in users:
    user["friends"] = []

for i,j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    return len(user["friends"])

total_connection = sum(number_of_friends(user) for user in users)

number_of_users = len(users)

average_connections = total_connection / number_of_users

number_of_friends_by_id = [(user["id"], number_of_friends(user) )for user in users]

sort = sorted(number_of_friends_by_id,
       reverse=True)

def friends_of_friend_ids_bad(user):
    return  [foaf["id"]
             for friend in user["friends"]
             for foaf in friend["friends"]]
    
def not_the_same(user, other_user):
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    return all(not_the_same(friend,other_user)
               for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
            for friend in user["friends"]
            for foaf in friend["friends"]
            if not_the_same(user, foaf)
            and not_friends(user, foaf))


    

# print(friends_of_friend_ids(users[3]))