n = int(input())
story = []
for _ in range(n):
    story.append(input().split(' '))

story_sort = sorted(story, key=lambda x : x[0])
for i in range(len(story_sort)):
    print(story_sort[i][1])