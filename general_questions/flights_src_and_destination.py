# GOA->BAN
# COK->MUM
# MUM->KOL
# KOL->GOA

a = [['GOA', 'BAN'], ['COK', 'MUM'], ['MUM', 'KOL'], ['KOL', 'GOA']]

src = set()
dest = set()

for i in a:
    src.add(i[0])
    dest.add(i[1])

result = []
for i in a:
    if i[0] not in dest:
        result.insert(0, i[0])
    if i[1] not in src:
        result.insert(len(result) - 1, i[1])

print(result[0], " to ", result[1], "should be COK to BAN")
