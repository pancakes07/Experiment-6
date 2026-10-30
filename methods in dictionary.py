JOB = {
    "Name": "Swarnit",
    "Age": 19,
    "Post": "Dta Analys",
    "Salary":70000 
    }
print("Keys")
print(JOB.keys())

print("Values")
print(JOB.values())

print("Items:")
print(JOB.items())

print("Names:",JOB.get("Name"))
print("Marks",JOB.get("marks","Not Available"))

JOB.update({"Age":18, "Marks":9})

print("After Updating")
print(JOB)

