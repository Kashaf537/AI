class Trapezoid:
    def __init__(self,a,b,h):
        self.a=a
        self.b=b
        self.h=h
    
    def Area(self):
        return 0.5*(self.a+self.b)*self.h
    
class Parallelogram:
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def AreaP(self):
        return self.base*self.height
    
        
class Comparison:
    def __init__(self):
        self.result={}

    def add_result(self,shape_name,area):
        self.result[shape_name]=area
    
    def largest_area(self):
        max_shape=max(self.result,key=self.result.get)
        return max_shape,self.result[max_shape]
    
    def display(self):
        for shape,area in self.result.items():
            print(f"{shape}:{area}")

if __name__=="__main__":
    comp=Comparison()

    trapezoid=Trapezoid(10,3,4)
    parallelogram=Parallelogram(8,7)

    comp.add_result("Trapezoid",trapezoid.Area())
    comp.add_result("Parallelogram",parallelogram.AreaP())

    print("Areas of shapes:")
    comp.display()

    shape,area=comp.largest_area()
    print(f"Shape with largest area: {shape}:({area})")

                
