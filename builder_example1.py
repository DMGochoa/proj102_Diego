from abc import ABC, abstractclassmethod

class Product():
    def __init__(self) -> None:
        self.parts = []

class IBuilder(ABC):
    
    @abstractclassmethod
    def build_part_a():
        pass
    
    @abstractclassmethod
    def build_part_b():
        pass
    
    @abstractclassmethod
    def build_part_c():
        pass
    
    @abstractclassmethod
    def get_result():
        pass
    
class Builder(IBuilder):
    
    def __init__(self) -> None:
        self.product = Product()
    
    def build_part_a(self):
        self.product.parts.append('a')
        return self
    
    def build_part_b(self):
        self.product.parts.append('b')
        return self
    
    def build_part_c(self):
        self.product.parts.append('c')
        return self
    
    def get_result(self):
        return self.product
        
class Director:
    """ Se encarga de dirigir la construccion """
    def construct():
        obj_construct = Builder().build_part_a().build_part_c().build_part_b().get_result()
        return obj_construct
    
if __name__ == '__main__':
    producto = Director.construct()
    print(producto.parts)