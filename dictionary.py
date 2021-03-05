#Key-value pairs
index_dict={
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six"
}

print(index_dict.get(5, "Not a valid key"))
#get(key, default value)
print(index_dict.get(100, "Not a valid key"))
