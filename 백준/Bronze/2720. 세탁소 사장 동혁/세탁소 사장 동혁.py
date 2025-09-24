quarter = 25
dime = 10
nickel = 5
penny = 1

t = int(input())
for i in range(t):
    c = int(input())
    quarter_n = c//quarter
    c = c%quarter
    dime_n = c//dime
    c = c%dime
    nickel_n = c//nickel
    c = c%nickel
    penny_n = c//penny
    print(quarter_n, dime_n, nickel_n, penny_n)