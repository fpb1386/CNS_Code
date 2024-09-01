import random
import os

# 写文件
def write_txt(name, content):
    path = os.getcwd() + '\\' + name + '.txt'

    if os.path.exists(path):
        print(name + '文件存在，覆盖原文件')
    else:
        print(name + '文件不存在，创建文件')

    with open(path, 'w', encoding='utf8') as f:  # 写入新文件
        for i in content:
            f.write(i + '\n')
        f.close()

# 读文件
def read_txt(name):
    content = []
    # 注释代码提供文件名称输入即可
    # with open(os.getcwd()+"\\"+name+".txt","r",encoding='utf8') as f:
    with open(name, "r", encoding='utf8') as f:
        for i in f.readlines():
            # i = i.strip('\n')
            i = i.rstrip('\n')
            content.append(i)
    f.close()
    return content

# Unicode数据编码为二进制
def to_two(content):
    content_two = []
    for i in content:
        n = []
        for j in i:
            # ord()返回当前字符十进制数字
            j = bin(ord(j)).replace('0b', '')
            n.append(j)
        content_two.append(n)

    return content_two

# 二进制还原成unicode数据
def two_return(content_two):
    tip = 0
    content_return = []
    for i in content_two:
        n = ''
        for j in i:
            # chr 返回当前整数对应的 ASCII 字符
            j = ''.join([chr(i) for i in [int(j, 2)]])

            # 原本打算在转换的时候处理这些特殊情况
            #             if(('\n' in j) or ('\r' in j)):
            #                 j = j.replace('\n','\\n')
            #                 j = j.replace('\r','\\r')

            n += j
        content_return.append(n)
    return content_return

# 生成密钥
def pro_secretkey(plaintext):
    plaintext_two = to_two(plaintext)

    #  密钥二进制储存
    secretkey = []

    for i in plaintext_two:
        tip = []
        for j in i:
            key = ''
            # 密钥生成在4-15位随意生成
            for l in range(random.randint(4, 15)):
                key += str(random.randint(0, 1))

            # 密钥碎片（总密钥一部分）如果0开头
            if (key.startswith('0')):  # 开头如果为0，往前添置一个1
                key = '1' + key
                num = random.randint(2, len(key) - 1)
                key = key[:num] + key[num + 1:]  # 随机删除一个数字

            # 密钥碎片中包含'\','\n','\r'，随机删除碎片一位数字
            #                             并在末尾加11（也是防止出现上述情况）
            if (key == '1011100' or key == '1010' or key == '1101'):
                num = random.randint(2, len(key))
                key = key[:num] + key[num + 1:]  # 随机删除一个数字
                key += '11'
            tip.append(key)
        secretkey.append(tip)

        # 记录密钥

    write_txt('一次密钥', two_return(secretkey))

    return two_return(secretkey)

def XOR_process(reference, change):
    # 内容变为二进制数据
    reference_two = to_two(reference)
    change_two = to_two(change)
    # 进行异或
    text_return = []
    for i in range(len(reference_two)):
        tip = []
        for j in range(len(reference_two[i])):
            # ^ 需要数据位int（10进制）类型
            #  结果为字符串形式
            k = bin(int(reference_two[i][j], 2) ^ int(change_two[i][j], 2))[2:]
            tip.append(k)
        text_return.append(tip)
    # 返回异或后的内容
    return two_return(text_return)

if __name__ == "__main__":
    # 读取明文
    name = '一次明文'
    path = os.getcwd() + "\\" + name + ".txt"
    plaintext = read_txt(path)
    print('明文：', plaintext)
    # 密钥生成
    secretkey = pro_secretkey(plaintext)
    print('密钥：', secretkey)
    # 密文生成
    ciphertext = XOR_process(secretkey, plaintext)
    print('密文：', ciphertext)
    # 密文记录
    write_txt('一次密文', ciphertext)
    # 解密
    plaintext_new = XOR_process(secretkey, ciphertext)
    print('解密后：', plaintext_new)
