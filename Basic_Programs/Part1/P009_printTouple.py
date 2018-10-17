"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
exam_st_date = (28, 8, 2017)
print("The examination will start from : {}".format('/'.join(map(str,exam_st_date))))

"""
output:
The examination will start from : 28/8/2017
"""