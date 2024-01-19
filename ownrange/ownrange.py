class my_range:
    def __init__(self,start=0,stop=None,step=1):
        if stop is None:
            raise TypeError("range acepted atleast 1 argument ,got 0")
        self.start=start
        self.stop=stop
        self.step=step

    def __iter__(self):
        return my_range_iterator(self)   
    
class my_range_iterator:
    def __init__(self,iterable_obj):
        self.iterable_obj=iterable_obj

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable_obj.start < self.iterable_obj.stop:
            result=self.iterable_obj.start
            self.iterable_obj.start+=self.iterable_obj.step
            return result
        else:
            raise StopIteration
        
for ele in my_range(10,-1):
    print(ele)