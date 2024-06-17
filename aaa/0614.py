f = open("aaa/test.txt", 'a', encoding="utf-8")
# ../ 는 파이썬 폴더 기준으로 한칸 더 상위로 감
# 두칸 더 상위로 가려면 ../../
f.write("\nhi")
# f.write('zzzzzzz')
# a = f.read()
# print(a)
f.close()

f = open("aaa/test.txt", 'r', encoding="utf-8")
a = f.readline()
print(a)
a = f.readlines()
print(a)
f.close()