#1.Custom Range
'''
Dimiourgia kai tou step
def custom_range(start,end,step):
      a=start
      c=step
      L=[a]
      for i in range(start,end):
         b=a+c
         a=b
         L.append(b)
      return L
    
print(custom_range(1,10,2))


def custom_range(start,end,step):
    L=[]
    for i in range(start,end,step):
        L.append(i)
    return L
x=custom_range(10,100,5)
print(x)


#2.Larger than Sum

def larger_than_sum(L):
    s=0
    m=[]
    for i in range(len(L)):
        for x in range(i+1,len(L)):
              s=s+L[x]
              if L[i]>s:
                 m[i]=True
              else:
                 m[i]=False
    for i in range(len(m)+1):
        if m[i]==False:
            return False
        else:
            return True 

L=[10,4,2,1]
print(larger_than_sum(L))


#Solution

def larger_than_sum(L):
    for i in range(len(L)-1):#thelo mexri to proteleutaio
        s=0
        for z in range(i+1,len(L)):
            s= s + L[z]
        if L[i]<=s:
            return False
    return True

L=[10,4,2,1]
print(larger_than_sum(L))           


#me sum
def larger_than_sum(L):
    for i in range(len(L)-1):#thelo mexri to proteleutaio
        if L[i]<=sum(L[i+1:]):
            return False
    return True


#3.isPalindrome
#prospatheia
def isPalindrome(L):
    if len(L)%2==0:
        T=L.reverse()#prepei prota na kaneis copy ti lista giati tin antistrefei kai tin idia
        if T==L:
            m=True
        else:
            m=False
    else:
        for i in range(len(L)+1):
            if L[i]==L[len(L)-i]:
               m=True
            else:
               m=False
    return m

L=[1,1,2,3,3]
print(isPalindrome(L))

#Solutions
      
def palindrome(L):
    for i in range(int(len(L)/2)):#to kano int giati to mesaio stoixeio de me peirazei
        if L[i]!=L[len(L)-1-i]:
            return False
    return True

def palindrome_2(L):
    R=[]
    for x in L:
        R.insert(0,x)#pairno ton antistrofo
    if L==R:
        return True
    return False


def palindrome_3(L):
    R=L.copy()
    R.reverse()
    if L==R:
       return True
    return False

def palindrome_4(L):
    R=L[int(len(L)/2)+1:]
    R.reverse()
    return L[:int(len(L)/2)]==R


L=[3,2,6,2,3]


print(palindrome(L))
print(palindrome_3(L))
print(palindrome_2(L))
print(palindrome_4(L))
'''
#4. Rock Scissors Paper

import random

L=['Rock','Scissors','Paper']
computer_points=0
player_points=0

while computer_points!=3 and player_points!=3:
      computer_choice=random.choice(L)
      player_choice=input('Choose: ')
      while player_choice not in L:#player_choice!='Rock' and player_choice!='Scissors' and player_choice!='Paper'
            player_choice=input('Wrong input!Choose between Rock,Scissors,Paper: ')
 
      if ((player_choice==L[0]and computer_choice==L[1]) or
          (player_choice==L[1]and computer_choice==L[2]) or
          (player_choice==L[2]and computer_choice==L[0])):
           print('Player wins the round')
           player_points=player_points+1

      elif ((player_choice==L[1]and computer_choice==L[0]) or
            (player_choice==L[2]and computer_choice==L[1]) or
            (player_choice==L[0]and computer_choice==L[2])):
            print('Computer wins the round')
            computer_points=computer_points+1

      else:
           print('It\'s a draw!')

if computer_points==3:
    print('Computer wins!')

if player_points==3:
    print('Player wins!')




































        
        
        
        
