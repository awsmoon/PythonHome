#student_output.py

def output(student) :
    print(f"{student['name']}\t{student['kor']}\t{student['eng']}", end='\t')
    print(f"{student['math']}\t{student['total']}\t{student['avg']:.2f}\t{student['grade']}")