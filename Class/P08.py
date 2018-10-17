"""
Write a Python class to reverse a string word by word.
Input string : 'hello .py'
Expected Output : '.py hello'
"""
class py_solution:
    def rev(self,strs):
        return ' '.join(reversed(strs.split()))

strs="hello .py"
print(py_solution().rev(strs))