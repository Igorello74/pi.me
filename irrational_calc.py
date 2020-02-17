"""Add classes calculating irrational numbers (as Pi, e, and so on).
Also, define abstract class IrrationalSerial and IrrationalDirect.
The first one is used to create the buffer of the irrational number,
when we need all the digits serially. The second one (if present) is used
when decoding - we don't need to save a big buffer, we can just take required
digits on go, in case if the constant allows, of course.
"""

from abc import ABC, abstractmethod

# class Irrational(ABC):
#     class Serial(ABC):


class _Pi(ABC):
    '''
    An abstract class for a Pi generator.
    '''

    @abstractmethod
    def __init__(self, num=None):
        pass
    
    @abstractmethod
    def __iter__(self):
        '''
        A generator returning an iterator
        of digits of pi after the decimal point.
        If num is presented, returns [num] digits of the Pi 
        after the decimal point,
        else no limit's set.
        Note: this doesn't include the first "3." part.
        '''
    
    @classmethod
    def print_n_digits_of_pi(cls, n):
        '''
        Prints n digits of pi after the decimal point.
        '''
        
        print('3.', end='')
        
        for digit in cls(n):
            print("0123456789ABCDEF"[digit], end='')
        
        print()
    

class BBP1(_Pi):
    '''
    Calculates digits of the Pi after the decimal point
    using the Bailey–Borwein–Plouffe formula
    (https://en.m.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula).
    It's the first implementation of the formula.
    '''
    
    def __init__(self, num=None):
        if num:
            self.iterator = range(num)
        else:
            from itertools import count
            self.iterator = count()


    def __iter__(self):
        n, d = 0, 1
        
        for N in self.iterator:
            xn = (120*N**2 + 151*N + 47)
            xd = (512*N**4 + 1024*N**3 + 712*N**2 + 194*N + 15)
            n = ((16 * n * xd) + (xn * d)) % (d * xd)
            d *= xd
            yield 16 * n // d


class BBP2(_Pi):
    '''
    Calculates digits of the Pi after the decimal point
    using the Bailey–Borwein–Plouffe formula
    (https://en.m.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula).
    It's the second implementation of the formula (the fastest one).
    '''

    def __init__(self, num=None):
        if num:
            self.iterator = range(1, num+1)
        else:
            from itertools import count
            self.iterator = count()


    def __iter__(self):
        a, b = 0, 1
        
        ak = 120 * 0**2 + 151 * 0 + 47
        bk = 512 * 0**4 + 1024 * 0**3 + 712 * 0**2 + 194 * 0 + 15
        
        a = 16 * a * bk + ak * b
        b = b * bk
        digit, a = divmod(a, b)
        
                
        for k in self.iterator:
            ak = 120 * k**2 + 151 * k + 47
            bk = 512 * k**4 + 1024 * k**3 + 712 * k**2 + 194 * k + 15
            
            a = 16 * a * bk + ak * b
            b = b * bk
            digit, a = divmod(a, b)
            yield digit
    
    
def _measure_timings(num_of_runs=10, num_of_digit=100):
    from timeit import timeit
    print(
      "\tThe first method's timing is", 
      timeit(lambda: BBP1.print_n_digits_of_pi(num_of_digit),
             number=num_of_runs)
      / num_of_runs
    )
    print(
      "\tThe second method's timing is",
      timeit(lambda: BBP2.print_n_digits_of_pi(num_of_digit),
             number=num_of_runs)
      / num_of_runs
    )


if __name__ == "__main__":
    _measure_timings()