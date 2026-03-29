#advisor.py

def analyzing_marks(marks):
    if marks <= 40:
       return("Weak")
    elif marks <= 60:
       return( "Average")
    elif marks <= 80:
       return( "Good")
    else:
       return( "Excellent")


def suggesting_time(marks):
    if marks <= 40:
        time = "3-4 hrs/day"
    elif marks <= 60:
        time = "2-3 hrs/day"
    elif marks <= 80:
        time = "1-2 hrs/day"
    else:
        time =  "1 hr/day"
        return time


def giving_advice(subject, marks):
    if marks <= 40:
       return(f"Focus heavily on {subject}.\n"
                "Practice questions daily and revise all topics.")
    elif marks <= 60:
       return(f"Improve {subject} with regular question practice.\n"
                "Revision is very important.")
    elif marks <= 80:
       return(f"Analyze mistakes in {subject}.\n"
                "Revise concepts thoroughly.")
    else:
       return(f"{subject} is strong. Revise consistently.\n"
               "question practice if needed")

