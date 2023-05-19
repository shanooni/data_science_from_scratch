tweet = {
       "user" : "joelgrus",
       "text" : "Data Science is Awesome",
       "retweet_count" : 100,
       "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

# dictionary and methods

for key in tweet.keys():
    print(key)
    
for value in tweet.values():
    print(value)

for key,value in tweet.items():
    print(f"{key} : {value}")