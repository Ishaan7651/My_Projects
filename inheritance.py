
class employee():
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation
        print(self.name, self.age, self.designation)

class programmer(employee):
    def show_language(self,language):
        self.language = language
        
        print(f"The programmer uses {self.language}")




a = employee("Ishaan",19,"Director")
b = employee("Radhe",19,"CEO")
c = employee("John",25,"Manager")
d = employee("Emily",30,"Supervisor")
e = employee("David",28,"Team Lead")
f = employee("Sophia",22,"Developer")
g = employee("Michael",35,"Project Manager")
h = employee("Emma",27,"Designer")
i = employee("James",33,"Analyst")
j = employee("Olivia",29,"Coordinator")
k = employee("Daniel",31,"Engineer")
l = employee("Ava",26,"Consultant")
m = employee("Logan",24,"Administrator")
n = employee("Isabella",32,"Specialist")
o = employee("Alexander",23,"Accountant")
p = employee("Mia",34,"Auditor")
q = employee("Benjamin",21,"HR Manager")
r = employee("Charlotte",36,"Marketing Director")
s = employee("Lucas",20,"Sales Representative")
t = employee("Amelia",37,"Operations Manager")
u = employee("Henry",38,"Finance Director")
v = employee("Harper",39,"Legal Advisor")
w = employee("Ethan",40,"Customer Service Manager")
x = employee("Evelyn",41,"Business Development Manager")
y = employee("Jack",42,"Quality Assurance Specialist")
z = employee("Grace",43,"Training Coordinator")
aa = employee("William",44,"Logistics Coordinator")
ab = employee("Liam",45,"IT Manager")
ac = employee("Victoria",46,"Research Analyst")
ad = employee("Sofia",47,"Product Manager")
ae = employee("Luna",48,"Operations Director")
af = employee("Chloe",49,"Supply Chain Manager")
ag = employee("Aiden",50,"Compliance Officer")
ah = employee("Zoe",51,"Risk Manager")
ai = employee("Gabriel",52,"Technical Lead")
aj = employee("Nora",53,"Recruiter")
ak = employee("Dylan",54,"Procurement Manager")
al = employee("Madison",55,"Business Analyst")
am = employee("Carter",56,"Public Relations Manager")
an = employee("Scarlett",57,"Customer Success Manager")
ao = employee("Luke",58,"Social Media Manager")
ap = employee("Ellie",59,"Event Coordinator")
aq = employee("Jayden",60,"Executive Assistant")


b = programmer("Japman",19,"Freind")
b.show_language("C++")