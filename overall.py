def student_averages(data):
    result={}

    for student, grades in data.items():
        avg= sum(grades.values())/len(grades)
        result[student]=round(avg)
    return result

def assignment_averages(data):
    result={}

    for student in data:
        assignments = data[student].keys()
        break
    for assignment in assignments:
        total=0
        count=0
        for student in data:
           total += data[student][assignment]
           count += 1
        result[assignment] =round(total/count)
    return result
def initialize_dict(name, grades):
    return {name: grades}