animal_dict = {"name": "rufus", "type": "dog"}
print("The keys are:", end = " ")
for a in animal_dict.keys():
    print(a, end = "-",sep = "-",)

print()
print("The values are:", end = " ")
for i in animal_dict.values():
    print(i, end = "-",sep = "-",)

print()
print("Both keys and values are:", end = " ")
for i in animal_dict.items():
    print("("+list(i)[0]+":"+list(i)[1]+")", end = "-",sep = ":",)



