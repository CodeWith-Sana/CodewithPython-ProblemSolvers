expl ={
    "name": "sana" ,
    "age" : 20,
    "id" : "216102"
}
print(expl)
print(expl["age"])
expl["gender"] = "F"
print(expl)
expl.pop('age')
print(expl)
print(expl.get("name"))