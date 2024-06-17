f = open("test.txt", 'w')
for i in range(1, 11) :
    sentence = "%d번째 줄입니다.\n" %i
    f.write(sentence)
f.close()

a = open("test.txt", 'r')
for i in range(1,11) :
    data = a.readline() #파일을 닫기 전까지 한 줄 읽고
    print(data, end="") #한 줄 출력
    # end 쓰면 줄간 공백 없이 출력가능
a.close()