import base64

alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

teststr = 'abcddddsssd'

def myBase64(src):
    length = len(src)
    ret = bytearray()
    r = 0
    for offset in range(0,length,3):
        if offset + 3 <= length:
            target = src[offset:offset + 3]
        else:
            target = src[offset:]
            r = 3 - len(target)
            target = target + '\x00' * r

        tmp = int.from_bytes(target.encode(),'big')
        #tmp = hex(tmpbyte) #'0x616263'

        for i in range(18,-1,-6):
            if i == 18:
                index = tmp >> i
            else:
                index = tmp >> i & 0x3F
            ret.append(alphabet[index])

        for i in range(1,r+1):
            ret[-i] = 0x3D
    return ret



print(myBase64(teststr))

print(base64.b64encode(teststr.encode()))
