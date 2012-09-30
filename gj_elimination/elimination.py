#coding: utf-8

'''Solving system of linear equations with Gauss-Jordan elimination'''

from frac import Frac


class Equation(list):
    def reduce_n(self, n):
        '''Reduce the nth element to 1'''
        r = self[n]
        for i in range(len(self)):
            self[i] /= r

    def __sub__(self, other):
        if isinstance(other, Equation):
            return Equation([a - b for a, b in zip(self, other)])
        else:
            raise NotImplemented

    def __mul__(self, other):
        if isinstance(other, Frac):
            return Equation([self[i] * other for i in range(len(self))])
        else:
            raise NotImplemented


class Equations(list):
    multi_answer_symbol = 'k'

    def __str__(self):
        rep = ''
        for i in range(len(self)):
            rep += ('%s\t' * len(self[i])) % tuple(self[i])
            rep.rstrip()
            rep += '\n'
        return rep.rstrip('\n')

    def __repr__(self):
        return self.__str__()

    def append(self, other):
        if isinstance(other, Equation):
            if len(self) == 0:
                super(Equations, self).append(other)
            else:
                if len(other) == len(self[-1]):
                    super(Equations, self).append(other)
                else:
                    raise WrongEquationError
        else:
            raise NotSupportedError

    def validate(self, equation):
        '''Validate if the line is possible,
        @ret: 1 possible
              0 multi-answer
              -1 no answer'''
        for i in range(len(equation)-1):
            if not equation[i].is_zero():
                return 1
        if equation[-1].is_zero():
            return 0
        else:
            return -1

    def __solve(self):
        '''Solve the equations with G-J method'''
        for n in range(len(self)):
            # NOTICE FIXME
            # is possible that the MultiAnswersError had raised,
            # but the other line still not be solved?
            # maybe can debug it with printing the line number
            # when MultiAnswersError is raised
            #
            #
            # BUG CASE FIXME
            # 1.
            #
            # 1 -2 3 -1 2
            # -2 5 -1 2 4
            # -1 1 -2 1 8
            # which answer should be:
            # -21+k, -7, 3, k
            check = self.validate(self[n])
            if check == -1:
                raise NoAnswerError
            elif check == 0:
                raise MultiAnswersError
            
            try:
                self[n].reduce_n(n)
            except ZeroDivisionError:
                raise NoAnswerError

            for line in range(len(self)):
                if line != n:
                    self[line] -= self[n] * self[line][n]

        return [self[i][-1] for i in range(len(self))]

    def __multi_answer(self):
        '''Handle multi-answer answer'''
        for n in range(len(self)):
            if self.validate(self[n]) == 0:
                zline = n
                break
        ret = []
        for line in range(len(self)):
            if line != zline:
                solve = '%s' % self[line][-1]
                d = self[line][zline]
                if d.is_minus():
                    d *= -1
                    operator = '+'
                else:
                    operator = '-'
                solve += '%s%s%s' % (operator, d, self.multi_answer_symbol)
                ret.append(solve)
            else:
                ret.append(self.multi_answer_symbol)
        return ret

    @property
    def solve(self):
        try:
            return self.__solve()
        except MultiAnswersError:
            return self.__multi_answer()
        except NoAnswerError:
            return 'No answer.'


class WrongEquationError(Exception):
    pass


class NotSupportedError(Exception):
    pass


class NoAnswerError(Exception):
    pass


class MultiAnswersError(Exception):
    pass
