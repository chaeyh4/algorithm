s_list = list(input())

for s in s_list:
    if s.islower():
        print(s.upper(), end = "")
    else:
        print(s.lower(), end = "")