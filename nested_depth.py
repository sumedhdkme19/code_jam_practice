def inputing():
    t = int(input())
    return t

def get_num_list(string):
    num_list = [int(a) for a in string]
    return num_list

def mod(a, b):
    d = a - b
    if d >= 0 :
        return d
    else:
        return -1 * d

def greater(a, b, string):
    string = string + mod(a,b)*'(' + str(b)
    return string

def lesser(a, b, string):
    string = string + mod(a,b) * ')' + str(b)
    return string

def process(num_list):
    b = num_list[0]
    string = (num_list[0]) * '(' + str(num_list[0])
    for i in range(0, len(num_list) - 1):
        a = num_list[i]
        b = num_list[i+1]
        if (b >= a):
            string = greater(a, b, string)
        elif (b < a):
            string = lesser(a, b, string)
    string = string + b*')'
    return string
        
    
if __name__ == '__main__' :
    t = inputing()
    for i in range(t):
        string = input()
        num_list = get_num_list(string)
        answer = process(num_list)
        print('Case #{}: {}'.format(i+1, answer))
