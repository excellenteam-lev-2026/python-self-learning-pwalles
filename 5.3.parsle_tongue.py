def parsle_tongue(path):
    with open(path,'rb') as f:
        while True:
            byte = f.read(1)
            if not byte:
                break
            yield byte[0]

if __name__ == "__main__":
    file_path="resources\\logo.jpg"
    word=""
    for b in parsle_tongue(file_path):
        if ord('a') <= b <= ord('z'):
            word += chr(b)
        elif b == ord('!'):
            if len(word)<5:
                word=""
            else:
                word+='!'
                print(word)
                word=""
        else:
            word=""
        
