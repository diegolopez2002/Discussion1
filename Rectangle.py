num_rectangle = 0

class Rectangle:

    def __init__(self, width, height):

        num_rectangle += 1  
        self.width = width
        self.height = height
  
    def get_area(self):

        area = self.width * self.height
        return area

    def get_num_rectangle():

        return num_rectangle
