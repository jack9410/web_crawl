
def isEnglish(input_s):

    words = input_s.split(" ")
    print(words)
    for a in words:
        for b in a:
            if not ord('a') <= ord(b.lower()) <= ord('z'):
                continue
            else:
                print(a)
                break


input_s = '영어 korean 한글 english'
isEnglish(input_s)