d = {"employee" : [{"firstName": "John" , "lastName" : "Doe"}, {"firstName": "Anna", "lastName" : "Smith"},
                    {"firstName" : "Peter", "lastName": "Jones" }], 
     "Owners": [{"firstName" : "Jack", "lastName": "petter"} , {"firstName": "Jessy" , "lastName": "Petter"}]}


# print Anna
Second_first_name = d["employee"][1]["firstName"]
print(Second_first_name)

#here we have two keys (employee and Owners and the values of that two keys are listes, those listes contains dictionaries)
for k in d.keys():
    List_temp=d[k]
    for dict_temp in List_temp:
      if(dict_temp['firstName'] == "Alexendra"):
         print("Alexendra has been found")
      else:
         print("Alexendra has not been found")
     
   
