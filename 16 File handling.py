file=open("shopping_list.txt", "r")
content=file.read()
file.close()
print(content)

# repr
print(repr(content))

# Sort the list of items in alphabetical order
items = content.split("\n")
items.sort()

# for loop
for item in items:
    print(f"- {item}")

# write to a new file

items="milk\nbread\neggs\ncheese\nbutter\napples\noranges\ntomatoes\nlettuce\ncereal"
new_file=open("sorted_shopping_list.txt", "w")
new_file.write(items)
new_file.close()   
print(items)

#append to a file

items="\nbananas\npears\ngrapes"
new_file=open("sorted_shopping_list.txt", "a")
new_file.write(items)
new_file.close()
print(items)

# read the updated file

updated_file=open("sorted_shopping_list.txt", "r")
updated_content=updated_file.read()
updated_file.close()
print(updated_content)


# Create a new file only

file = open("new_file.txt", "x")
file.write("arun")
file.close()
print("new_file.txt created successfully.")


