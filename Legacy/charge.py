import sys
sys.stdin = open('charge.txt', 'r')

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]


def find_max_charge(c_list):
    m_charge = 0
    for i in c_list:
        if chargers[i][3] > m_charge:
            m_charge = chargers[i][3]
    return m_charge

def bfs():
    global charge_sum
    ar, ac, br, bc = 0, 0, 9, 9
    for _ in range(M+1):
        # 0초부터이므로 M+1을 해주고 유저 이동정보 뒤에 각각 [0]을 붙여주었음
        # print(_, '초')
        # print(ar, ac, br, bc, _)
        a_list, b_list = list(), list()

        for i in range(A):
            r, c, charge_dis, power = chargers[i]
            DA, DB = abs(ar-r)+abs(ac-c), abs(br-r)+abs(bc-c)
            if DA <= charge_dis:
                a_list.append(i)
                # print('a 충전가능', i, '번 충전기')
            if DB <= charge_dis:
                b_list.append(i)
                # print('b 충전가능', i, '번 충전기')
        # 여기 도달하기 전에 충전 가능 충전기의 충전량을 리스트로 a, b 따로 저장해서 모든 경우의 수를 구하고, 최대값으로 충전하면된다.
        # print(a_list, b_list)
        if a_list and b_list:
            m_charge = 0
            for i in a_list:
                for j in b_list:
                    charge = 0
                    if i == j:  # 같은 충전기인 경우
                        charge = chargers[i][3]
                    else:  # 같은 충전기가 아닌 경우
                        charge = chargers[i][3] + chargers[j][3]
                    if charge > m_charge:
                        m_charge = charge
            # print(m_charge)
            charge_sum += m_charge

        elif a_list:
            # print(find_max_charge(a_list))
            charge_sum += find_max_charge(a_list)
        elif b_list:
            # print(find_max_charge(b_list))
            charge_sum += find_max_charge(b_list)
        ar, ac, br, bc = ar+dr[userA[_]], ac+dc[userA[_]], br+dr[userB[_]], bc+dc[userB[_]]
        # print()



for tc in range(1, int(input())+1):
    M, A = map(int, input().split())
    userA = list(map(int, input().split()))+[0]
    userB = list(map(int, input().split()))+[0]
    # print('사용자 A의 이동 정보 :', userA)
    # print('사용자 B의 이동 정보 :', userB)
    chargers = list()
    for i in range(A):
        X, Y, C, P = map(int, input().split())
        chargers.append((Y-1, X-1, C, P))
    # print(chargers)
    # for i in range(10):
    #     print(arr[i])
    # print()
    charge_sum = 0
    bfs()

    print("#{} {}".format(tc, charge_sum))


#1 1200
#2 3290
#3 16620
#4 40650
#5 52710

