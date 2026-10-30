JOB = {
    "Name": "Swarnit",
    "Age": 19,
    "Post": "Data Analyst",
    "Salary": 70000
    
    }


#add an element
JOB["ID"] = "25BCAR0141"

print("After adding",JOB)


#updating an element
JOB["Age"] = 18

print("After Updating",JOB)

#Deleting an element
del JOB["Salary"]

print("After Deleting",JOB)
