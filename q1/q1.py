def questions_marks(strParam: str) -> bool:
    '''
    Exemplos:

    Test 1
    >>> questions_marks("aa6?9") 
    False

    Test 2
    >>> questions_marks("arrb6???4xxbl5???eee5")
    True

    Test 3
    >>> questions_marks("acc?7??sss?3rr1??????5")
    True

    Test 4
    >>> questions_marks('5??aaaaaaaaaaaaaaaaaaa?5?5')
    False

    Test 5
    >>> questions_marks("9???1???9??1???9")
    False

    Test 6
    >>> questions_marks("8asd1")
    False

    ''' 
    size = len(strParam)
    if size == 0: return False
    resp = False    
    i = 0
    while ( i < size): 
        # achou o primerio digito
        if strParam[i].isnumeric():
            a = int(strParam[i])
            count = 0
            i+=1
            # procurando ? ou proximo digito
            while (i < size):          
                c = strParam[i]
                # achou o proximo digito
                if c.isnumeric():
                    i-=1
                    b = int(c)
                    # so verifica se a soma for 10
                    if a+b == 10: 
                        if count == 3:
                            # print(a, b, a + b, count)
                            resp = True 
                        else: 
                            # print(a, b, a + b, count)
                            return False
                    break
                # acho ?  
                if c == '?':
                      count+=1
                i+=1
        i+=1    
    return resp

if __name__ == '__main__':
    string = 'arrb6???4xxbl5???eee5'
    print(questions_marks(string))