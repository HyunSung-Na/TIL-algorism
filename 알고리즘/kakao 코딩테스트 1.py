import re

def solution(new_id):
    new_id_1st = new_id.lower()
    new_id_2st = re.sub('[~!@#$%^&*=+:?,\(\)\[\]\`\']', '', new_id_1st)
    new_id_3st = []
    for id in new_id_2st:
        if id == '.':
            if new_id_3st:
                if new_id_3st[-1] == '.':
                    continue
                else:
                    new_id_3st.append(id)
            else:
                new_id_3st.append(id)
        else:
            new_id_3st.append(id)
    new_id_3st = ''.join(new_id_3st)
    new_id_4st = list(new_id_3st)
    if new_id_4st[0] == '.':
        del new_id_4st[0]
    elif new_id_4st[-1] == '.':
        del new_id_4st[-1]
    if not new_id_4st:
        new_id_4st.append('a')
    if len(new_id_4st) > 15:
        new_id_4st = new_id_4st[:15]
        if new_id_4st[-1] == '.':
            del new_id_4st[-1]
    elif len(new_id_4st) <= 2:
        while len(new_id_4st) <= 2:
            new_id_4st.extend(new_id_4st[-1])
    answer = ''.join(new_id_4st)
    return answer


new_id = "...!@BaT#*..y.abcdefghijklm]"
new_id1 = "abcdefghijklmn.p"
new_id2 = "z-+.^."
new_id3 = "abcdefghijklmn.p"
print(solution(new_id))