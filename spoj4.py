#postfix

#postfix

#precedence
precedence = {"+":1,"-":1,"*":2,"/":2,"^":3}

#returns true for every lesser precedence ex in the stack sequence is like *,+  then it will return true and * will be popped
def isGreater(index,top):
    try:
     a=int(precedence[index])
     b=int(precedence[top])
     return True if a<=b else False
    except KeyError:
        return False
#converts to postfix
def infix_to_posttfix(exp):
     postfix=[]
     stack = Stack()
     for i in exp:
         if i=='(':
             stack.push(i)
         elif i.isalpha():
             postfix.append(i)
         elif i==')':
             while ((stack.top!=-1) and stack.peek()!='('):
                 a=stack.pop()
                 postfix.append(a)
             if stack.top!=-1 and stack.peek()!='(':
                 return -1
             else:
                 stack.pop()
         else:
             while stack.top!=-1 and isGreater(i,stack.peek()):
                 postfix.append(stack.pop())
             stack.push(i)
     while stack.top!=-1:
         postfix.append(stack.pop())
     return postfix

#stack implementation
class Stack:
    def __init__(self):
        self.top=-1
        self.st=[]

    def push(self,item):
        self.top+=1
        self.st.append(item)

    def pop(self):
        if self.top!=-1:
             self.top-=1
             return self.st.pop()
        else:
            self.top=-1

    def peek(self):
        if self.top!=-1:
           return self.st.__getitem__(self.top)

    def print(self):
        print(self.st)

#driver function
def main():
    n=int(input())
    for i in range(n):
       inf = str(input())
       pos = infix_to_posttfix(inf)
       for j in pos:
           print(j,end='')
       print()

if __name__ == '__main__':
         main()

#sample input                
#(a+(b*c))
#((a+b)*(z+x))
#((a+t)*((b+(a+c))^(c+d)))

#output
#abc * +
#ab + zx + *
#at + bac + +cd + ^ *
