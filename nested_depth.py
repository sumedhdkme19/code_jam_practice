def inputing():
    t = int(input())
    return t

def get_paranthesis(i):
    s = ''
    if i == 0 :
            return str(i)
    s = ('({})'.format(i))
    while i >= 2 :
        s = '(' + s + ')'
        i = i - 1
    return s

'''def check_for_is_previous_one(i, s):
    previous = s[-2: -3: -1]
    if i == 1 :
        sub = s[0: -1] + '1)'
    return sub'''

def check_for_is_previous(i, s):
    sub = s
    flag = True
    previous = s[-(i+1): -(i+2): -1]
    if (previous == str(i) and i > 0) :
        sub = s[0: -i] + ('{}'.format(i)) + i*(')')
        flag = False
    elif (int(previous) < i and i > 0) :
        sub = s[0: -i] + ('{}'.format(i)) + i*(')')
        flag = False
    return sub, flag
    
def pranthesis(istr):
    string = ''
    workable = [int(i) for i in istr]
    length = len(workable)
    string = get_paranthesis(workable[0])
    for i in range(1, length) :
        string, flag = check_for_is_previous(workable[i], string)
        if flag :
                ch = get_paranthesis(workable[i])
                string = string + ch
    return string
    
if __name__ == '__main__' :
    t = inputing()
    for i in range(t):
        string = input()
        ans = pranthesis(string)
        print('Case #{}: {}'.format(i+1, ans))
