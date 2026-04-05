def student_averages(data):
    result={}

    for student, grades in data.items():
        avg= sum(grades.values())/len(grades)
        result[student]=round(avg)
    return result

def assignment_averages(data):
    result={}

    for student in data:
        assigments = data[student].keys()
    for assigment in assigments:
        total=0
        count=0
        for student in data:
           total += data[student][assigment]
           count += 1
        result[assigment] =round(total/count)
    return result
def initialize_dict(name, grades):
    return {name: grades}