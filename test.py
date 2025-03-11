
def modify_list(list_):
    list_.append("new")
    list_ = ["completely", "new"]

items = ["original"]
modify_list(items)
print(items)
