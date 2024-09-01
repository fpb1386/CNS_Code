import random
import math

def isprime():
#判断是否素数，直至输入为素数为止
    count = 1
    while count:
        n = int(input("输入一个质数(p)："))
        for i in range(2, n):
           if n % i == 0:
                print("%d不是一个质数！" % n)
                break
        else:
            return n

def get_generator( p):
#获取一个原根
#素数必存在至少一个原根
#g^(p-1) = 1 (mod p)当且仅当指数为p-1的时候成立
    a=2
    while 1:
        if a**(p-1) % p == 1:
            num = 2
            mark = 0
            while num < p-1:
                if a**num % p == 1:
                    mark = 1
                num += 1
        if mark == 0:
            return a
        a += 1
        
def get_cal(a, p, rand):
#获得计算数
    cal = (a**rand) % p
    return cal
    
def get_key(cal_A,cal_B,p):
#获得密钥
    key = (cal_B ** cal_A ) % p
    return key

def Is_sameKey(S_a, S_b):
#判断密钥是否相同
    if S_a == S_b:
        print("A所得的密钥与B相同")
    else:
        print("A所得的密钥与B不相同")


if __name__ == "__main__":
    p = isprime()
    a = get_generator(p)
    print("p的一个原根为%d"%a)
    rand_A = random.randint(0, p-1)
    cal_A = get_cal(a, p, rand_A)
    print("A随机数%d得到的计算数为%d" % (rand_A, cal_A))
    rand_B = random.randint(0, p-1)
    cal_B = get_cal(a, p, rand_B)
    print("B随机数%d得到的计算数为%d" % (rand_B, cal_B))
    S_a = get_key(rand_A, cal_B, p)
    print("A的密钥为%d" % S_a)
    S_b = get_key(rand_B, cal_A, p)
    print("B的密钥为%d" % S_b)
    Is_sameKey(S_a, S_b)
