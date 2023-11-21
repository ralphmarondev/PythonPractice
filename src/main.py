if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(student_marks.get(query_name))
    # score_list = student_marks.get(query_name[scores])
    # result = [lambda x: x + i for i in score_list] / len(score_list)
    #
    # print(result)
    result = '{:.2f}'.format(sum(student_marks[query_name]) / len(student_marks[query_name]))
    print(result)

