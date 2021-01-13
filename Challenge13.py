data = '''1011416
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,911,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,827,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19'''
vals = data.split("\n")

start = int(vals[0])
val = list()
nos = vals[1].split(",")

for no in nos:
    if no != 'x':
        val.append(int(no))
        
ans = 1
c = True

while c:
    for no in val:
        if start % no == 0:
            c = False
            ans = no
    start += 1
#part1
print((start-1-1011416)*ans)

def inverse(M,m_i):
    inv = 1
    while(True):
        if (inv*(M/m_i))%m_i == 1:
            return inv
        inv += 1
M = 1
for no in val:
    M *= no

m_a = {}
value = 0
for no in nos:
    if(no.isnumeric() and int(no) in val):
        m_a[int(no)] = value
    value += 1

result = 0
for m in m_a:
    inv = inverse(M,m)
    #print((m_a[m]*inv*(M/m)),result)
    result += (m_a[m]*inv*(M/m))
    #print(m,m_a[m],inv,result,M)
print(result%M)
#Answer is 640856202464541
"""
def ext_gcd(a, b):
    x = 1
    y = 0
    x1 = 0
    y1 = 1
    a1 = a
    b1 = b

    while b1 > 0:
        q = a1 // b1
        x, x1 = x1, x - q*x1
        y, y1 = y1, y - q*y1
        a1, b1 = b1, a1 - q*b1

    return x, y

    
if __name__ == '__main__':
    n = int(input())
    t = input().split(',')
    divs = []
    mx = [-1, -1]
    lcm = 1
    for i in range(len(t)):
        if t[i] == 'x':
            continue

        t[i] = int(t[i]) 

        k = i
        k %= t[i]
        k = t[i] - k
        k %= t[i]

        divs.append([int(t[i]), k])
        lcm *= int(t[i])
        if mx[0] == -1 or divs[-1][0] > mx[0]:
            mx = divs[-1]

    print(divs)
    
    while len(divs) > 1:
        n1, a1 = divs[-1]
        n2, a2 = divs[-2]

        divs.pop()
        divs.pop()
        m1, m2 = ext_gcd(n1, n2)
        x = a1*m2*n2 + a2*m1*n1
        x %= n1*n2

        if x < 0:
            x += n1*n2
        divs.append([n1*n2, x])
        print(divs)
    print(divs[0][1])
"""

