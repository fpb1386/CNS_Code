def Determination(d):       #决定要对字符串进行加密还是解密
    if d == 0:
        return Encryption()
    elif d == 1:
        return Deciphering()
 
def Encryption():       #加密
    s = input("请输入需要加密的文字:\n")
    for i in s:
        c=''
        if 'a' <= i <= 'z':
            c += chr(ord('a') + (ord(i) - ord('a') + 3) % 26)
            print(c, end='')
        elif 'A' <= i <= 'Z':
            c += chr(ord('A') + (ord(i) - ord('A') + 3) % 26)
            print(c, end='')
        else:
            c += i
            print(c, end='')
def Deciphering():      #解密
    c,s = input("请输入需要解密的文字:\n"),''  #变量定义及函数返回值
    for i in c:
        if 'a' <= i <= 'z':
            s += chr(ord('a') + (ord(i) - ord('a') - 3) % 26)
        elif 'A' <= i <= 'Z':
            s += chr(ord('A') + (ord(i) - ord('A') - 3) % 26)
        else:
            s += i
    return print(s)
 
def main():      #开启整个程序的入口，启动第一步调用Determination函数
    print("仅限加解密英文字母")
    sel = eval(input("请选择加密或者解密模式(输入0为加密模式，输入1为解密模式):"))
    Determination(sel)
 
main()
