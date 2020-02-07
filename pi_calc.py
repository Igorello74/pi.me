class _Pi:
    '''
    An abstract class for a Pi generator.
    '''
    
    def pi(num=None):
        '''
        A generator returning an iterator
        of digits of pi after the decimal point.
        If num is presented, returns [num] digits of the Pi 
        after the decimal point,
        else no limit's set.
        Note: this doesn't include the first "3." part.
        '''
           
        raise NotImplementedError()
    
    @classmethod
    def print_n_digits_of_pi(cls, n):
        '''
        Prints n digits of pi after the decimal point.
        '''
        
        print('3.', end='')
        
        for digit in cls.pi(n):
            print("0123456789ABCDEF"[digit], end='')
        
        print()
    
    class Meta:
        abstract = True

class BBP1(_Pi):
    '''
    Calculates digits of the Pi after the decimal point
    using the Bailey–Borwein–Plouffe formula
    (https://en.m.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula).
    It's the first implementation of the formula.
    '''
    
    @staticmethod
    def pi(num=None):
        
        n, d = 0, 1
        
        if num:
            iterator = range(num)
        else:
            from itertools import count
            iterator = count()
            
        for N in iterator:
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
    
    @staticmethod
    def pi(num=None):
        
        a, b = 0, 1
        
        if num:
            iterator = range(1, num+1)
        else:
            from itertools import count
            iterator = count()
        
        ak = 120 * 0**2 + 151 * 0 + 47
        bk = 512 * 0**4 + 1024 * 0**3 + 712 * 0**2 + 194 * 0 + 15
        
        a = 16 * a * bk + ak * b
        b = b * bk
        digit, a = divmod(a, b)
        
                
        for k in iterator:
            ak = 120 * k**2 + 151 * k + 47
            bk = 512 * k**4 + 1024 * k**3 + 712 * k**2 + 194 * k + 15
            
            a = 16 * a * bk + ak * b
            b = b * bk
            digit, a = divmod(a, b)
            yield digit
    
    
def measure_timings():
    from timeit import timeit
    print("\tThe first method's timing is", timeit(lambda: BBP1.print_n_digits_of_pi(100), number=10))
    print("\tThe second method's timing is", timeit(lambda: BBP2.print_n_digits_of_pi(100), number=10))

if __name__ == "__main__":
    measure_timings()