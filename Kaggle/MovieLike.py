def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    print(sum(percentage_liked[4:8]))/(sum(list_liked))
    # TODO: Complete the function
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])
print(percentage_liked)
