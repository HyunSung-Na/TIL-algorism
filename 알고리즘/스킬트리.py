def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        check = False
        skillqueue = list(skill)
        for to_skill in skills:
            if to_skill in skillqueue:
                if to_skill == skillqueue[0]:
                    del skillqueue[0]
                    check = True
                else:
                    check = False
                    break
        else:
            check = True
        if check:
            answer += 1
    return answer

