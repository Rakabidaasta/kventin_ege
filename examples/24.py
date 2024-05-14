# 59790

f = open("24.txt").read()
f = f.replace("\n", "")
inds = [i for i in range(len(f)) if f[i] == "T"]
min_s = len(f)
for i in range(len(inds) - 209):
    start = inds[i]
    end = inds[i + 209]
    s = f[start : end + 1]
    min_s = min(len(s), min_s)
print(min_s)