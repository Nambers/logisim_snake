re = "v2.0 raw\n"
while True:
    s = input()
    if s == "q":
        fo = open("x", "w")
        fo.write(re)
        fo.close()
        break
    if s == "qq":
        fo = open("x1", "w")
        fo.write(re)
        fo.close()
        break
    re += str(hex(int(s,2))).replace("0x", "").zfill(8) + "\n"
print(re)