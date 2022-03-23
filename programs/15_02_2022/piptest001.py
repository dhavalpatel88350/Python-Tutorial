from gtts import gTTS


a=open('001.txt','r')
b=a.read()
print(b)
res = ''.join([i for i in b if not i.isdigit()])


s = gTTS(res)
s.save("test.mp3")
