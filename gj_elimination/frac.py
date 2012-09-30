#coding: utf-8


class Frac(object):
    '''A fraction number'''
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError
        self.numer = numerator
        self.denom = denominator
        self.reduction()

    def __str__(self):
        # TODO: display format
        self.reduction()
        if self.denom == 1 or self.numer == 0:
            return '%d' % self.numer
        else:
            #print '%f' % (float(self.numer) / float(self.denom))
            return '%d/%d' % (self.numer, self.denom)

    def __repr__(self):
        return self.__str__()

    def gcd(self, a, b):
        while (a % b):
            tmp = b
            b = a % b
            a = tmp

        return b

    def lcm(self, a, b):
        return a * b / self.gcd(a, b)

    def is_zero(self):
        return self.numer == 0

    def is_minus(self):
        self.reduction()
        return self.numer < 0

    def reverse(self):
        return Frac(self.denom, self.numer)

    def reduction(self):
        if self.denom * self.numer < 0:
            self.denom = abs(self.denom)
            self.numer = -abs(self.numer)
        else:
            self.denom = abs(self.denom)
            self.numer = abs(self.numer)
        g = self.gcd(abs(self.numer), abs(self.denom))
        self.numer /= g
        self.denom /= g

    def denomination(self, other):
        if isinstance(other, Frac):
            l = self.lcm(self.denom, other.denom)
            self.numer *= l / self.denom
            self.denom = l
            other.numer *= l / other.denom
            other.denom = l
        else:
            raise NotImplemented

    def __add__(self, other):
        if isinstance(other, Frac):
            self.denomination(other)
            return Frac(self.numer + other.numer, self.denom)
        if isinstance(other, int):
            return self.denomination(self.numer + other * self.denom, self.denom)
        else:
            raise NotImplemented

    def __sub__(self, other):
        if isinstance(other, Frac):
            self.denomination(other)
            return Frac(self.numer - other.numer, self.denom)
        if isinstance(other, Int):
            return Frac(self.numer - other * self.denom, self.denom)
        else:
            raise NotImplemented

    def __mul__(self, other):
        if isinstance(other, Frac):
            return Frac(self.numer * other.numer, self.denom * other.denom)
        if isinstance(other, int):
            return Frac(self.numer * other, self.denom)
        else:
            raise NotImplemented

    def __div__(self, other):
        if isinstance(other, Frac):
            if other.is_zero():
                raise ZeroDivisionError
            else:
                return Frac(self.numer * other.denom, self.denom * other.numer)
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError
            else:
                return self.__div__(Frac(other))
        else:
            raise NotImplemented


def frac_factory(raw_num):
    '''Return a frac base on the input'''
    if not isinstance(raw_num, str):
        raw_num = str(raw_num)

    #: is a fraction
    if raw_num.find('/') != -1:
        numer, denom = raw_num.split('/')
        # TODO
        # numer and denom from the input are supposed as int instead of float
        # maybe using int casting's ValueError can improve it
        return Frac(int(numer), int(denom))
    #: is a float
    if raw_num.find('.') != -1:
        # TODO
        # use mathematic method to calculate the len of the b part
        # rather than len()
        a, b = raw_num.split('.')
        denom = 10 ** len(b)
        numer = float(raw_num)
        numer *= denom
        return Frac(numer, denom)
    #: suppose it's an int
    else:
        return Frac(int(raw_num), 1)
