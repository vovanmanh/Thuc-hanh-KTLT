print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
class Circle(object):
 def __init__(self, r):
  self.radius = r
###############################
 def area(self):
  return self.radius**2*3.14
aCircle = Circle(2)
print (aCircle.area())
