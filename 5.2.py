# %%
data = './data/5.1.txt'
rules, pages = [], []
is_rule = True
count = 0

def check_rule(page, rules):
    ok_rules = True
    for rule in rules:
        try:
            ok_rules *= page.index(rule[0]) < page.index(rule[1])
        except:
            ok_rules *= True
    return ok_rules


def correct_page(page, rules):
    while check_rule(page,rules) == False:
        for rule in rules:
            try:
                index1, index2 = page.index(rule[0]),  page.index(rule[1])
                if  index1 > index2:
                    page[index1], page[index2] = page[index2], page[index1]
            except:
                pass
    return page

for line in open(data,'r'):
    if line == '\n':
        is_rule = False
    elif is_rule == True:
        rules.append([int(l) for l in line.replace('\n','').split('|')])
    else:
        pages.append([int(l) for l in line.replace('\n','').split(',')])
        
for page in pages:
    ok_rules = check_rule(page, rules)
    if ok_rules == False:
        page = correct_page(page, rules)
        count += page[len(page)//2]

print(count)