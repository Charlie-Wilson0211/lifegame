import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class lifegame():
    def __init__(self,ground):
        self.begin = ground
        self.array = self.begin.copy()
        self.temp_array = self.begin.copy()
        self.width,self.height = self.array.shape
        self.__version__="1.0"
        
    def __iter__(self):
        self.array = self.begin.copy()
        self.temp_array = self.begin.copy()
        return self
                
    def check_num(self,array,i,j):
        return array[max(0,i-1):min(i+2,self.width),max(0,j-1):min(j+2,self.height)].sum()-array[i,j]
    
    def change(self,array,i,j,num):
        if num == 3:
            return 1
        elif num == 2:
            return array[i,j]
        else:
            return 0
        
    def update(self,array):
        temp_array =array.copy()
        for i,line in enumerate(array):
            for j,cell in enumerate(line):
                temp_array[i,j]=self.change(array,i,j,self.check_num(array,i,j))
        array =temp_array
        return array
                
        
    def __next__(self):
        self.array,self.temp_array =self.temp_array,self.update(self.array)
        return self.array
    
    def __getitem__(self,n):
        if isinstance(n,int):
            array = self.begin.copy()
            for _ in range(n):
                array = self.update(array)
            return array
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            array = self.begin.copy()
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(array)
                array = self.update(array)
            return L
        
    def __getattr__(self,attr):
        if attr =="version":
            return self.__version__
        
    def __call__(self):
        print("This class is for LifeGame based on simple ruler")
