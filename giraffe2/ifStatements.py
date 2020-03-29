is_male= False
is_tall= False
if is_male or is_tall:
    print("You are a male or tall or both")


if is_male and is_tall:
    print("You are a male and tall")

elif is_male and not(is_tall):
    print("You are not tall")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are neither a male nor tall")




