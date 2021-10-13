book_title_list = []
book_cost_list = []

for i in range(0, 5):
    book_title_list.append(input("\nEnter title of book " + str(i+1) + ":"))
    book_cost_list.append(input("Enter cost of book " + str(i+1) + ":"))

running_cost = 0
for i in range(0, 5):
    running_cost += float(book_cost_list[i])

print("\nRunning cost of all 5 books is: $" + str(running_cost))
