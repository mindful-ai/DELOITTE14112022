>>>
>>> 
>>> [<expr> <loop> <condition>] 
  File "<stdin>", line 1
    [<expr> <loop> <condition>]
     ^
SyntaxError: invalid syntax
>>> [x**2 for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
>>> col = 'name,age,regid,phy,chem,math,bio,avg,rank\n'
>>> col.split(',')
['name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank\n']
>>> [c.strip() for c in col.split(',')]
['name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank']
>>> cols = [c.strip() for c in col.split(',')]
>>> r = 'Vijay,14,HPE001,99,98,97,36,0,0\n'
>>> rows = [row.strip() for row in r.split(',')]
>>> cols
['name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank']
>>> rows
['Vijay', '14', 'HPE001', '99', '98', '97', '36', '0', '0']
>>> zip(cols, rows)
<zip object at 0x00000208C42D3FC0>
>>> dict(zip(cols, rows))
{'name': 'Vijay', 'age': '14', 'regid': 'HPE001', 'phy': '99', 'chem': '98', 'math': '97', 'bio': '36', 'avg': '0', 'rank': '0'}    
>>> d = {'name': 'Vijay', 'age': '14', 'regid': 'HPE001', 'phy': '99', 'chem': '98', 'math': '97', 'bio': '36', 'avg': '0', 'rank': 
>>> d.keys()
dict_keys(['name', 'age', 'regid', 'phy', 'chem', 'math', 'bio', 'avg', 'rank'])
>>> ','.join(d.keys())
'name,age,regid,phy,chem,math,bio,avg,rank'
>>> ','.join(d.keys()) + "\n"
'name,age,regid,phy,chem,math,bio,avg,rank\n'
>>> ','.join(d.values()) + "\n"
'Vijay,14,HPE001,99,98,97,36,0,0\n'
>>> exit()

