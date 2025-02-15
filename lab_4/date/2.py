import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days = 1)
z = x + datetime.timedelta(days = 1)

print(x, "its today")
print(y, "its yesterday")
print(z, "and its tomorrow")