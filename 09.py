class Person(object):
    
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    
    def __str__(self):
        return "Person [name=%s, age=%d, address=%s]" % (self.name, self.age, self.address)
    
    
    def _wakeUp(self):
        print(f'{self.name},起床!')
        
    
    def _eat(self):
        print(f'{self.name},吃菜、扒饭!')
    
    
    def _wush(self):
        print(f'{self.name},刷牙、洗脸!')
    
    
    def _sleep(self):
        print(f'{self.name},睡觉!')
        
        
    @classmethod
    def Count(cls):
        print(f'学生总数为{cls.count}人')
        
        
class Student(Person):
    count = 0
    
    def __init__(self, name, age, address):
        super().__init__(name, age, address)
        Student.count += 1
        
        
    def __str__(self):
        return "学生 [name=%s, age=%d, address=%s]" % (self.name, self.age, self.address)
    
    
    def __loginAccount(self):
        print(f'{self.name},账号登录成功')
        
    
    def __learn(self):
        print(f'{self.name},看视频、写代码!')
        
    
    def oneday(self):
        print(f'{self.name}一天的学习生活')
        self._wakeUp()
        self._wush()
        self._eat()
        self.__loginAccount()
        self.__learn()
        self._eat()
        self.__learn()
        self._eat()
        self._wush()
        self._sleep()
    
    @classmethod
    def Count(cls):
        print(f'学生总数为{Student.count}人')


class Teacher(Person):
    count = 0
    
    def __init__(self, name, age, address):
        super().__init__(name, age, address)
        Teacher.count += 1
    
    
    def __str__(self):
        return "老师 [name=%s, age=%d, address=%s]" % (self.name, self.age, self.address)
    
    
    def punchTheClock(self):
        print(f'{self.name}今日打卡成功')
    
    
    def work(self):
        print(f'{self.name}授课、答疑、写代码')
        
    
    def oneday(self):
        print(f'{self.name}一天的工作生活')
        self._wakeUp()
        self._wush()
        self._eat()
        self.punchTheClock()
        self.work()
        self._eat()
        self.work()
        self._eat()
        self._wush()
        self._sleep()
    
    
    @classmethod
    def Count(cls):
        print(f'老师总数为{Teacher.count}人')


xiaoming = Student('小明', 18, '北京')
limei = Student('丽媚', 19, '上海')
guoming = Student('国明', 20, '广州')
zhanshi = Student('展示', 21, '深圳')
didi = Student('弟弟', 22, '杭州')
xiaoming.oneday()
Student.Count()
print('*', '*' * 50, '*')
zhangjunfei = Teacher('张俊飞', 30, '北京')
lilu = Teacher('李露', 31, '上海')
huoshinan = Teacher('霍世南', 32, '广州')
zhangjunfei.oneday()
Teacher.Count()
