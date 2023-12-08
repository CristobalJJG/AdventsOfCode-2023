map1 = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
}
    
def main(string) :
    def localize_numbers(word:str):
        res = [0,0]
        index = [len(word)-1, 0]
            
        # Find words
        wl = word.lower()
        # print(wl)
        for (key, value) in map1.items():
            i = wl.find(key)
            # print(key,'-- i:',i, ',', 'i0:', index[0], ',', 'i1:', index[1] )
            if i != -1:
                if(wl.count(key) > 1):
                    i2 = wl.rfind(key)
                    if i2 < index[0]: res[0] = value; index[0] = i2
                    if i2 > index[1]: res[1] = value; index[1] = i2
                if i < index[0]: res[0] = value; index[0] = i
                if i > index[1]: res[1] = value; index[1] = i
            if index[0] == 0 and index[1] == len(word)-1: break;
        if(res[0] == 0): res[0] = res[1]
        if(res[1] == 0): res[1] = res[0]
        return int(str(res[0])+''+str(res[1]))
    
    # Start of the main function
    sum = 0
    for x in string.split('\n'):
        s = localize_numbers(x)
        sum += s
        print(s)
        # print('-----------------')
    print('Suma:', sum)
        
# Main branch
f = open('./Day1/input.txt', 'r')
phrase = '''two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen'''

text = f.read()
main(text);
f.close()
