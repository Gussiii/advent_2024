data = './data/5.1.txt'

rules, pages = [], []
is_rule = True
count = 0

for line in open(data,'r'):
    if line == '\n':
        is_rule = False
    elif is_rule == True:
        rules.append([int(l) for l in line.replace('\n','').split('|')])
    else:
        pages.append([int(l) for l in line.replace('\n','').split(',')])

def check_rule(page, rule):
    try:
        return page.index(rule[0]) < page.index(rule[1])
    except:
        return True

for page in pages:
    
    ok_rules = True
    for rule in rules:
        ok_rules *= check_rule(page, rule)
    
    if ok_rules:
        count += page[len(page)//2]

print(count)

