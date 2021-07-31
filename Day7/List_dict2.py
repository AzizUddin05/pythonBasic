Person1 = {'id' : 's-001','name' : 'Nashid Pervez','email' : 'python603@daffodil.ac'}
Person2 = {'id' : 's-002','name' : 'Afrin Sultana','email' : 'afrin603@daffodil.ac'}
Person3 = {'id' : 's-003','name' : 'Mehedi Hasan','email' : 'python603@daffodil.ac'}
Person4 = {'id' : 's-004','name' : 'Aziz Uddin','email' : 'python603@daffodil.ac'}
Person5 = {'id' : 's-005','name' : 'Naushin Anjum','email' : 'python603@daffodil.ac'}

Persons = [Person1,Person2,Person3,Person4,Person5]

for p in Persons :
    print('Id number : %s' %(p['id']))
    print('Name : %s' %(p['name']))
    print('Email : %s' %(p['email']))
    print('='*50)
