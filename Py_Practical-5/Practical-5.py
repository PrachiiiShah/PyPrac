#20CE133 - Prachi Shah

"""You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. """

def swap_case(s):
    
    Output = '';
    for char in s:
        if(char.isupper()==True):
            Output = Output + (char.lower());
        elif(char.islower()==True):
             Output = Output + (char.upper());
        else:
             Output = Output + char;
    return Output;
  

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)