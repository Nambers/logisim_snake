re = "v2.0 raw\n"
while True:
    s = input()
    if s == "q":
        break
    re += str(hex(int(s,2))).replace("0x", "") + "\n"
fo = open("x", "w")
fo.write(re)
fo.close()
print(re)