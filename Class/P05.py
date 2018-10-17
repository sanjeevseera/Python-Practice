"""
Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4
"""
class py_solution:
    def indices(self,numbers):
        for i in range(len(numbers)-1):
            if numbers[i]+numbers[i+1] == 50:
                return (i,i+1)
        else:
            return 'None'
            

numbers=[10,20,10,40,50,60,70]
print("index1=%d, index2=%d"%py_solution().indices(numbers))