"""some grade related utils"""


def letter_grade(gpa):
    """return the letter grade of a GPA."""
    # TODO: your if/elif chain here
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
