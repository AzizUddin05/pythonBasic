Persons = [
        {'id' : 's-001','name' : 'Nashid Pervez','email' : 'python603@daffodil.ac'},
        {'id' : 's-002','name' : 'Afrin Sultana','email' : 'afrin603@daffodil.ac'},
        {'id' : 's-003','name' : 'Mehedi Hasan','email' : 'python603@daffodil.ac'},
        {'id' : 's-004','name' : 'Aziz Uddin','email' : 'python603@daffodil.ac'},
        {'id' : 's-005','name' : 'Naushin Anjum','email' : 'python603@daffodil.ac'}
        ]

print('%10s %30s %20s'%('Id Number','Name','Email Address'))
print('='*50)
for p in Persons :
    print('%-10s %-30s %-20s'%(p['id'],p['name'],p['email']))
    print('-'*80)
    
 