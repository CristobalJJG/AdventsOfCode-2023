map = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
    
def main(string) :
    def localizeNumbers(word:str):
        res = [0,0]
        start = 0; end = len(word) - 1
        sf=False;ef = False

        while start <= end:
            if word[start] in map and not sf: res[0] = word[start]; sf = True
            if word[end] in map and not ef: res[1] = word[end]; ef = True
            if sf and ef: break;
            if not sf: start += 1; 
            if not ef: end -= 1
            
        return int(str(res[0])+''+str(res[1]))
    
    # Start of the main function
    sum = 0
    for x in string.split('\n'):
        sum += localizeNumbers(x)
    print('Suma:', sum)
        
# Main branch
f = open('./Day1/input.txt', 'r')
text = f.read()
main(text);
f.close()
