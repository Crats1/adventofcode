def read_input():
    with open('day6input.txt') as f:
        data = f.read().split('\n\n')
        return [group.split('\n') for group in data]

def count_questions_answered(grouped_answers):
    questions_answered = 0
    for group in grouped_answers:
        questions_answered += len(set([c for member in group for c in member]))
    return questions_answered
    # return sum([len(set([c for member in group for c in member])) for group in grouped_answers]) # One-liner solution

def count_questions_everyone_answered(grouped_answers):
    questions_everyone_answered = 0
    for group in grouped_answers:
        group_members = len(group)
        answers = [c for member in group for c in member]
        questions_answered = set([c for member in group for c in member])
        questions_everyone_answered += sum([answers.count(question) == group_members for question in questions_answered])
    return questions_everyone_answered

groups = read_input()
print('P1:', count_questions_answered(groups))
print('P2:', count_questions_everyone_answered(groups))