#/usr/bin/env python3
#-*- coding:utf-8 -*-


class Operation(object):
    '''定义操作父类'''
    def getresult(self):
        pass

class Add(Operation):
    '''加'''
    def getresult(self):
        result=self.numberA+self.numberB
        return result

class Sub(Operation):
    '''减'''
    def getresult(self):
        result=self.numberA-self.numberB
        return result

class Mul(Operation):
    '''乘'''
    def getresult(self):
        result=self.numberA*self.numberB
        return result

class Div(Operation):
    '''除'''
    def getresult(self):
        try:
            result=self.numberA/self.numberB
            return result
        except:
            print('ZeroDivisionError')
        
class Undef(Operation):
    def getresult(self):
        print('Undefine operation')
        return 0

class OperationFactory(object):
    '''简单运算工厂类'''
    def createOperation(self,op):
        if op=='+':
            oper=Add()
        elif op=='-':
            oper=Sub()
        elif op=='*':
            oper=Mul()
        elif op=='/':
            oper=Div()
        else:
            oper=Undef()
        return oper

if __name__=='__main__':
    op=input('operation:')
    numberA=int(input('a:'))
    numberB=int(input('b:'))
    factory=OperationFactory()
    cal=factory.createOperation(op)
    cal.numberA=numberA
    cal.numberB=numberB
    print(cal.getresult())
