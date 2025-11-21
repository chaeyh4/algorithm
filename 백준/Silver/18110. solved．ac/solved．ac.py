import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    level = 0
    opinion_list = []
    for _ in range(n):
        opinion = int(input())
        opinion_list.append(opinion)

    if n == 0:
        print(level)
    else:
        opinion_list.sort()
        cut = int(n * 0.15 + 0.5)

        # cut 이 0이면 그냥 전체 사용, 0보다 크면 양쪽 자르기
        if cut > 0:
            cut_list = opinion_list[cut:len(opinion_list) - cut]
        else:
            cut_list = opinion_list

        final_level = int(sum(cut_list) / len(cut_list) + 0.5)
        print(final_level)