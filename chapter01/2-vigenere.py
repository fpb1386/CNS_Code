letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 字母表
# 根据输入的key生成key列表
def Get_KeyList(key):
    key_list = []
    for ch in key:
        key_list.append(ord(ch.upper()) - 65)
    return key_list
# 加密函数
def Encrypt(message, key_list):
    cipher_text = ""
    i = 0
    for ch in message:  # 遍历明文
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha(): #明文是否为字母,如果是,则判断大小写,分别进行加密
            if ch.isupper():
                cipher_text += letter_list[(ord(ch) - 65 + key_list[i]) % 26]
                i += 1
            else:
                cipher_text += letter_list[(ord(ch) - 97 + key_list[i]) % 26].lower()
                i += 1
        else:  # 如果密文不为字母,直接添加到密文字符串里
           cipher_text += ch
    return cipher_text
# 解密函数
def Decrypt(cipher_text, key):
    decrypted_text = ""
    i = 0
    for ch in cipher_text:  # 遍历密文
        if 0 == i % len(key_list):
            i = 0
        if ch.isalpha(): #密文为否为字母,如果是,则判断大小写,分别进行解密
            if ch.isupper():
                decrypted_text += letter_list[(ord(ch) - 65 - key_list[i]) % 26]
                i += 1
            else:
                decrypted_text += letter_list[(ord(ch) - 97 - key_list[i]) % 26].lower()
                i += 1
        else:  # 如果密文不为字母,直接添加到明文字符串里
            decrypted_text += ch
    return decrypted_text

if __name__ == '__main__':
  message = "Common sense is not so common."
  key = "PIZZA"
  key_list = Get_KeyList(key)
  cipher_text = Encrypt(message, key_list)
  print("加密前的文本是:\n%s" % message)
  print("密文为:\n%s" % cipher_text)
  decrypted_text = Decrypt(cipher_text, key_list)
  print("明文为:\n%s" % decrypted_text)
