from database import database
from logic import func
def insert_gpa(Grades):
    calculated_GPA=func(Grades)
    db=database()
    cr=db.cursor()
    l=['name','CS','Math1','Discrete','Elctronics','Creative_thinking','Technical_writing']
    s=['%s']
    if Grades.name is not None:
        query=f"insert into calcs({' ,'.join(l)},GPA) values({','.join(s*8)})"
        values=list(getattr(Grades,col)for col in l)
        values.append(calculated_GPA)
        cr.execute(query,tuple(values))
    else:
         query=f"insert into calcs({' ,'.join(l[1:])},GPA) values({','.join(s*7)})"
         values=list(getattr(Grades,col) for col in l[1:])
         values.append(calculated_GPA)
         cr.execute(query,tuple(values))
    db.commit()
    cr.close()
    db.close()
    return{'Your GPA' : calculated_GPA}
    
    

    