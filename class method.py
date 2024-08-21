class employees:
    company_name = "Apple"
     
    @classmethod
    def change_name(lols,new):
        lols.company_name = new
        print(lols.company_name)

a = employees()
a.change_name("Tesla")
print(employees.company_name)


