s = input()
print(sum(int(x)**2 for x in range(int(s.split()[0]), int(s.split()[1])+1)))