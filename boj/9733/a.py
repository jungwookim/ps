valid_works = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']

def solution():
    dic = dict()
    total = 0
    while True:
        try:
            a = input().split()
            for ai in a:
                total += 1
                if ai in valid_works:
                    if ai in dic:
                        dic[ai] += 1
                    else:
                        dic[ai] = 1
        except:
            break

    print('Re', dic.get('Re', 0), format(dic.get('Re', 0) / total, '.2f'))
    print('Pt', dic.get('Pt', 0), format(dic.get('Pt', 0) / total, '.2f'))
    print('Cc', dic.get('Cc', 0), format(dic.get('Cc', 0) / total, '.2f'))
    print('Ea', dic.get('Ea', 0), format(dic.get('Ea', 0) / total, '.2f'))
    print('Tb', dic.get('Tb', 0), format(dic.get('Tb', 0) / total, '.2f'))
    print('Cm', dic.get('Cm', 0), format(dic.get('Cm', 0) / total, '.2f'))
    print('Ex', dic.get('Ex', 0), format(dic.get('Ex', 0) / total, '.2f'))
    print('Total', total, format(1.00, '.2f'))
solution()