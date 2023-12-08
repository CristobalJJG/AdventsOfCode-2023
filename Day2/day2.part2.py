def main(string) :
    lines = string.split('\n')
    res = 0
    # Format of the data 
    for l in lines:
        
        map1 = {
            'red': 0,
            'green':0,
            'blue': 0,
        }
        flag = True
        sets = l.split(': ')[1].split('; ')
        for s in sets:
            game = s.split(', ')
            if not flag: break
            for r in game:
                sec = r.split(' ')
                if(int(sec[0]) > int(map1[sec[1]])): 
                    map1[sec[1]] = sec[0]
                    
        power = 1;    
        for v in map1.values():
            power *= int(v)
        res += power
    print(res)
    
        
        
# Main branch
f = open('./Day2/input.txt', 'r')
example = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
text = f.read()
main(text);
f.close()
