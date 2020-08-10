def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        check = False
        skillqueue = list(skill)
        for j in i:
            if j in skillqueue:
                if j == skillqueue[0]:
                    del skillqueue[0]
                    check = True
                else:
                    check = False
                    break
            else:
                check = True
        if check:
            answer += 1

    return print(answer)

skill = "CBD"
skill_tree = ["BACDE", "CBADF", "AECB", "BDA","ACDDB","CAABGD"]
solution(skill,skill_tree)