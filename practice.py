# lambda function
# syntax:        lambda arguments : expression

def double(n):
    return lambda a: a * n

x = double(2)
y = x(11)
# print(y)

list1 = [10, 25, 30, 65, 45, 20, 64, 22, 100]
fitered = filter(lambda x: x > 40, list1)

print(fitered)
print(list(fitered))


# Another example
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

filtered_countries = filter(lambda country: country[1] > 300000000, countries)

result = list(filtered_countries)
print(result)