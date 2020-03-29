lucky_numbers = [4, 8, 15, 16, 23, 42]
friends= ["Kevin", "Karen", "Jim", "Jim", "Brad", "Toby"]

friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)


lucky_numbers.append(100)
print(lucky_numbers)

friends.insert(1,"Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)
print(friends.index("Kelly"))

friends= ["Kevin", "Karen", "Jim", "Jim", "Brad", "Toby"]
print(friends.count("Jim"))
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2=friends.copy()
print(friends2)

friends.clear()
print(friends)


