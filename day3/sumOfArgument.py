def sum_(*args):
    a=0
    for x in args:
        a+=x
    return a

print(sum_(2,5,8))
print(sum_())
print(sum_(2,3,5,5,6,6,7,7,8))