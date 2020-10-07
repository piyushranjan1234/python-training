address1 = {"state": "westBengal", "dist": "parganas", "city": "kolkatta"}
address2 = {"state": "delhiNCR", "dist": "south", "city": "delhi"}
dict1 = [{"firstName": "john", "secondName": "smith", "age": 45, "address": address1},
         {"firstName": "rahul", "secondName": "bindra", "age": 24, "address": address2}]
x=[x for x in dict1 if x["address"]["city"]=="kolkatta"]
print(x)
