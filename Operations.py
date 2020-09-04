from connection import MyDb


class operation():

    def add(self, a, b):
        return a + b

    def check_even_no(self, a):
        if a % 2 == 0:
            return True
        else:
            return False

