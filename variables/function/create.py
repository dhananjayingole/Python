# here marks_List passed is a Parameter
def marks_calculation(marks_List):
    total_marks = sum(marks_List)
    average_marks = total_marks / len(marks_List) if marks_List else 0
    return total_marks, average_marks

# Example usage:
marks = [85, 90, 78, 92, 88]
# heres marks passed is an Argument
total, average = marks_calculation(marks)   
print(f"Total Marks: {total}, Average Marks: {average}")

