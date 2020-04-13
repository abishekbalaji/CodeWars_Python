def delete_nth(order, max_e):
    count = 0
    for i in range(len(order)):
        check = order[i]
        print(f"First for loop check: {order[i]}")
        for j in range(len(order)):
            print(f"Before first if j: {j}")
            if check == order[j]:

                print(f"Inside first if : {order[j]}")
                count += 1
                if count > max_e:
                    print(f"Inside final if {order[j]}")
                    print(j)
                    order.pop(j)
                    count -= 1
        count = 0


l = [1, 2, 3, 2, 1, 4, 1, 2]
delete_nth(l, 2)
print(l)

