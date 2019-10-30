# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:17:33 2019

@author: DSU
"""

class MyBigIntegers:
    def __init__(self, input=None, base=10):
        if input is None:
            self.integer = '0'
        elif isinstance(input, list):
            self.integer = ''.join(str(x) for x in input)
        elif isinstance(input, str):
            self.integer = str(abs(int(input, base)))
    
    def __len__(self):
        return len(self.integer)
    
    def __add__(self, other) -> MyBigIntegers:
        carry = 0
        array = list()
        length = max(len(other), len(self))
        
        for a, b in zip(self.integer[::-1].ljust(length, '0'),\
                        other.integer[::-1].ljust(length, '0')):
            s = int(a) + int(b) + carry
            s, carry = s % 10, s // 10
            array.append(s)
        
        if carry: array.append(carry)
        return MyBigIntegers(input=array[::-1])
    
    def __mul__(self, other) -> MyBigIntegers:
        len1 = len(self) 
        len2 = len(other) 
        if other.integer == '0' or self.integer == '0': 
            return MyBigIntegers()
      
        result = [0] * (len1 + len2) 
        
        i_n1 = 0
        i_n2 = 0
      
        for i in range(len1 - 1, -1, -1): 
            carry = 0
            n1 = ord(self.integer[i]) - 48
      
            i_n2 = 0
      
            for j in range(len2 - 1, -1, -1): 
                n2 = ord(other.integer[j]) - 48
                summ = n1 * n2 + result[i_n1 + i_n2] + carry 
                carry = summ // 10
                result[i_n1 + i_n2] = summ % 10
                i_n2 += 1
      
            if (carry > 0): 
                result[i_n1 + i_n2] += carry 
      
            i_n1 += 1
        
        return MyBigIntegers(result[::-1])
            
    
    def ToString(self, base16=False):
        if base16:
            start = hex(int(self.integer))[2:]
            finish = list()
            length = len(start) - 1
            for i, x in enumerate(start[::-1]):
                finish.append(x)
                if i != length and i%4 == 3:
                    finish.append(':')
            
            return ''.join(finish[::-1])
                
        else:
            return self.integer

if __name__ == '__main__':
    
    A = ['523004898858735521', '220758617692186442', '460674828835159568',\
         '142038006856929955', '536121496772617388', '112137493324750603',\
         '690796069846053026', '814564078556167347', '180512479842461002',\
         '646588448516637981', '444556959154324505', '206725965987503988']
    B = ['810017810852848964', '69101654073787491', '235835651116434816',\
         '962022575760609851', '584994243195327903', '141893478896824908',\
         '278386261950154281', '413574972226298198', '437062588034587455',\
         '187818575705627797', '402813271607194236', '467620374047189121']
    C = ['1333022709711584485', '289860271765973933', '696510479951594384',\
         '1104060582617539806', '1121115739967945291', '254030972221575511',\
         '969182331796207307', '1228139050782465545', '617575067877048457',\
         '834407024222265778', '847370230761518741', '674346340034693109']
    
    for a, b, c in zip(A, B, C):
        assert (MyBigIntegers(a) + MyBigIntegers(b)).ToString() == c
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    