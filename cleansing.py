def remove_duplicate():
    """create an empty list to contain no duplicate"""
    duplicatelist = [1, 2, 2, 3, 4, 4, 5, 7,11, 5, 12, 12, 4]
    noduplicatelist = []
    for i in duplicatelist:
        if i not in noduplicatelist:
            noduplicatelist.append(i)
    print(noduplicatelist)
remove_duplicate()