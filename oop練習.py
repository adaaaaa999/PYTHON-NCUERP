class Jobs:
    def __init__(self):
        self.money = '資料不足' #工資
        self.time = '資料不足' #工時
        self.people = '資料不足' #產業人數

#====方法不可和變數名稱相同，會有衝突產生錯誤====
    
    def salary(self):
        print(f'工資: {self.money}')
    
    def work_hours(self):
        print(f'工時: {self.time}')

    def industry_people(self):
        print(f'產業人數: {self.people}')

class Nurse(Jobs):
    def name(self):
        print('護理師')

    def set_salary(self,money):
       self.money = money  # 將傳入的 money 值賦給 self.money
    
    def set_work_hours(self,work_hours):
        self.time = work_hours  # 將傳入的 work_hours 賦給 self.time

    def set_industry_people(self,industry_people):
        self.people = industry_people  # 將傳入的 industry_people 賦給 self.people

class Engineer(Jobs):
    def name(self):
        print('工程師')

    def set_salary(self,money):
       self.money = money  # 將傳入的 money 值賦給 self.money
    
    def set_work_hours(self,work_hours):
        self.time = work_hours  # 將傳入的 work_hours 賦給 self.time

    def set_industry_people(self,industry_people):
        self.people = industry_people  # 將傳入的 industry_people 賦給 self.people

b = Nurse()
b.set_salary('35000-50000')
b.set_work_hours('8-12')
b.set_industry_people('300000')
b.name()
b.salary()
b.work_hours()
b.industry_people()
c = Engineer()
c.set_salary('40000-60000')
c.set_work_hours('8-9')
c.set_industry_people('500000')
c.name()
c.salary()
c.work_hours()
c.industry_people()
    


