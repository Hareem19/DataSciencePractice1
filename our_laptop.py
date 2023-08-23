def hello():
    print("hello")
class Laptop():
    def __init__(self,color,ram,make,model,processor):
        self.color=color
        self.ram=ram
        self.make=make
        self.model=model
        self.processor=processor
    def spec(self):
        print(f"""
              ram: {self.ram}
              color: {self.color}
              make: {self.make}
              model: {self.model}
              processor: {self.processor}
              
              """)
    def get_color(self):
            print(f"The color of laptop is : {self.color}")
    def set_color(self, new_color):
            colors=["black","red","blue"]
            if new_color in colors:
                self.color-new_color
            else:
                print(f"This color of laptop is not available")
    def get_model(self):
            print(f"The model of laptop is : {self.model}")
    def set_model(self, new_model):
            models=["g2","g1","g3"]
            if new_model in models:
                self.model=new_model
            else:
                print(f"This model of laptop is not available")