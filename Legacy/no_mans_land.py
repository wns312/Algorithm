import sys
sys.stdin = open('no_mans_land.txt', 'r')


def p_set(idx, box_idx, height, remain):
    global max_height
    # 다 쌓아도 최대 높이가 안된다면? 리턴시킴


    # 모든 박스가 세팅 완료
    if box_idx == len(boxes):
        if height > max_height:
            max_height = height
        return

    # 박스 돌리기 완료
    if idx == 3:
        if height > max_height:
            max_height = height
        # 한 층 이상
        if box_idx and (boxes[box_idx][0] > boxes[box_idx - 1][0] or boxes[box_idx][1] > boxes[box_idx - 1][1]):
            return
        if height + remain <= max_height: return
        p_set(0, box_idx+1, height+boxes[box_idx][2], remain - boxes_max_height[box_idx])
        return

    for i in range(idx, 3):
        boxes[box_idx][idx], boxes[box_idx][i] = boxes[box_idx][i], boxes[box_idx][idx]
        p_set(idx+1, box_idx, height, remain)
        boxes[box_idx][idx], boxes[box_idx][i] = boxes[box_idx][i], boxes[box_idx][idx]


def change_boxes(idx):
    if max_b_length == max_height: return
    if idx == len(boxes):
        p_set(0, 0, 0, sum(boxes_max_height))
        return

    for i in range(idx, len(boxes)):
        boxes[idx], boxes[i] = boxes[i], boxes[idx]
        boxes_max_height[idx], boxes_max_height[i] = boxes_max_height[i], boxes_max_height[idx]
        change_boxes(idx+1)
        boxes[idx], boxes[i] = boxes[i], boxes[idx]
        boxes_max_height[idx], boxes_max_height[i] = boxes_max_height[i], boxes_max_height[idx]


# def check_heights(idx):
# #     idx 높이까지만 더해서 구한다


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    boxes = [list(map(int, input().split())) for _ in range(N)]
    boxes_max_height = [max(boxes[_]) for _ in range(N)] # 박스들의 가장 긴 길이
    max_b_length = sum(boxes_max_height)
    max_height = max(boxes_max_height)
    # print(boxes)
    # print(boxes_max_height)
    # 여기서 상자 위치를 바꿔주면서 재호출 해주면 됨 : 나중에~~
    # p_set(0, 0)
    change_boxes(0)
    print(max_height)
    print()
    print()
    # get_height(0)




#1 76
#2 158
#3 1181
#4 6897
#5 36700