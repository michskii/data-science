import numpy as np
data_type=[('name', 'S15' ),('Grade', int),('height',float)]
student_details=[('john', 10, 165), ('jane', 9, 159), ('doe', 11, 170),('mark', 8, 152),('sara', 10, 160)]
student=np.array(student_details,dtype=data_type)
print(f"original Array: {student}")
print(f"sorted by height:{np.sort(student, order='height')}")