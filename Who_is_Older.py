old = int(input())
m = 17
if old<m:
     x = m - old
     x = int(x)
     print("I'm older than you by " + str(x) + " years")
elif old == m:
     print("we're age mate")
else:
     x = old - m
     print("You are older than me by " + str(x) + " years")