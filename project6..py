from tkinter import *

def restart():
    global a
    a=['A','E',' ','E',' ','S',' ','H','O']
    canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
    text()
    text_input.delete(0.0,END)
    text_input.insert(0.0,'you just put restart button')

def text_match(x):
    f=open('file2.txt','r')
    k=f.readlines()
    print(x)
    for i  in k:
        for j in x:
            if(i==j):
                print(i)
                text_input.insert(0.0,'you made a word :'+i)
            
    f.close()
    

def text():
    
    t1=canvas.create_text(50,50,text=a[0],font="arial 35 bold",tags="text1",fill="black",activefill="red")
    t2=canvas.create_text(150,50,text=a[1],font="arial 35 bold",tags="text2",fill="black",activefill="red")
    t3=canvas.create_text(250,50,text=a[2],font="arial 35 bold",tags="text3",fill="black",activefill="red")
    t4=canvas.create_text(50,150,text=a[3],font="arial 35 bold",tags="text4",fill="black",activefill="red")
    t5=canvas.create_text(150,150,text=a[4],font="arial 35 bold",tags="text5",fill="black",activefill="red")
    t6=canvas.create_text(250,150,text=a[5],font="arial 35 bold",tags="text6",fill="black",activefill="red")
    t7=canvas.create_text(50,250,text=a[6],font="arial 35 bold",tags="text7",fill="black",activefill="red")
    t8=canvas.create_text(150,250,text=a[7],font="arial 35 bold",tags="text8",fill="black",activefill="red")
    t9=canvas.create_text(250,250,text=a[8],font="arial 35 bold",tags="text9",fill="black",activefill="red")


    
def twoside(u,d,l,r,ulc,drc,urc,dlc,t):
        global s
        s=aniket.get()
        aniket.set('')
        if(s=='down'):
            canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
            a[d]=a[t]
            a[t]=' '
            text()
            text_input.delete(0.0,END)
            text_input.insert(0.0,'you have entered  '+ s +'  button')

        elif(s=='up'):
            canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
            a[u]=a[t]
            a[t]=' '
            text()
            text_input.delete(0.0,END)
            text_input.insert(0.0,'you have entered  '+ s +'  button')
            
        elif(s=='uprightcorner'):
            canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
            a[urc]=a[t]
            a[t]=' '
            text()
            text_input.delete(0.0,END)
            text_input.insert(0.0,'you have entered  '+ s +'  button')

        elif(s=='left'):
           
            canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
            a[l]=a[t]
            a[t]=' '
            text()
            text_input.delete(0.0,END)
            text_input.insert(0.0,'you have entered  '+ s +'  button')

        elif(s=='right'):
            canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
            a[r]=a[t]
            a[t]=' '
            text()
            text_input.delete(0.0,END)
            text_input.insert(0.0,'you have entered  '+ s +'  button')     

        elif(s=='upleftcorner'):
            canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
            a[ulc]=a[t]
            a[t]=' '
            text()
            text_input.delete(0.0,END)
            text_input.insert(0.0,'you have entered  '+ s +'  button')

        elif(s=='downleftcorner'):
            canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
            a[dlc]=a[t]
            a[t]=' '
            text()
            text_input.delete(0.0,END)
            text_input.insert(0.0,'you have entered  '+ s +'  button')
            
        elif(s=='downrightcorner'):
            canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
            a[drc]=a[t]
            a[t]=' '
            text()
            text_input.delete(0.0,END)
            text_input.insert(0.0,'you have entered  '+ s +'  button')


        else:
            
           text_input.delete(0.0,END)
           text_input.insert(0.0,'chose your side left,right,up,down,uprightcorner,downrightcorner,upleftcorner,downleftcorner ')
   


    
def text1():
    
    if(a[1]==' 'and a[3]==' ')and a[4]==' ':
        
        twoside(0,3,0,1,0,4,0,0,0)
        
    elif (a[1]==' 'and a[4]==' '):
        twoside(0,0,0,1,0,4,0,0,0)
            
    elif (a[1]==' 'and a[3]==' '):
        twoside(0,3,0,1,0,0,0,0,0)
        

    elif (a[4]==' 'and a[3]==' '):
        twoside(0,3,0,0,0,4,0,0,0)

    elif a[1]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[1]=a[0]
        a[0]=' '
        text()
        text_input.delete(0.0,END)
    elif a[3]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[3]=a[0]
        a[0]=' '
        text()
        text_input.delete(0.0,END)

    else:
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[4]=a[0]
        a[0]=' '
        text()
        text_input.delete(0.0,END)

    l=[a[1]+a[2]+'\n',a[2]+a[1]+'\n',a[3]+a[4]+'\n',a[4]+a[3]+'\n',a[4]+a[5]+'\n'
       ,a[5]+a[4]+'\n',a[6]+a[7]+'\n',a[7]+a[6]+'\n',a[7]+a[8]+'\n',a[8]+a[7]+'\n'
       ,a[3]+a[6]+'\n',a[6]+a[3]+'\n',a[1]+a[4]+'\n',a[4]+a[1]+'\n',a[4]+a[7]+'\n'
       ,a[7]+a[4]+'\n',a[2]+a[5]+'\n',a[5]+a[2]+'\n',a[5]+a[8]+'\n',a[8]+a[5]+'\n'
     ,a[3]+a[7]+'\n',a[7]+a[3]+'\n',a[4]+a[8]+'\n',a[8]+a[4]+'\n',a[1]+a[5]+'\n'
       ,a[5]+a[1]+'\n',a[4]+a[2]+'\n',a[2]+a[4]+'\n',a[6]+a[4]+'\n',a[4]+a[6]+'\n'
       ,a[5]+a[7]+'\n',a[7]+a[5]+'\n',a[1]+a[3]+'\n',a[3]+a[1]+'\n'
       ,a[3]+a[4]+a[5]+'\n',a[5]+a[4]+a[3]+'\n',a[6]+a[7]+a[8]+'\n'
       ,a[8]+a[7]+a[6]+'\n',a[1]+a[4]+a[7]+'\n',a[7]+a[4]+a[1]+'\n'
       ,a[2]+a[5]+a[8]+'\n',a[8]+a[5]+a[2]+'\n',a[2]+a[4]+a[6]+'\n',a[6]+a[4]+a[2]+'\n']
       
    text_match(l)

   
def text2():
    
    
    if (a[0]==' ' and a[3]==' ')and a[4]==' ':
        twoside(0,4,0,0,0,0,0,3,1)

    elif a[4]==' ' and (a[5]==' 'and a[2]==' '):
        twoside(0,4,0,2,0,5,0,0,1)

    elif(a[3]==' ' and a[4]==' ')and a[5]==' ':
        twoside(0,4,0,0,0,5,0,3,1)

    elif(a[0]==' ' and a[2]==' ')and a[3]==' ':
        twoside(0,0,0,2,0,0,0,3,1)

    elif(a[0]==' ' and a[2]==' ')and a[4]==' ':
        twoside(0,4,0,2,0,0,0,0,1)

    elif(a[0]==' ' and a[2]==' ')and a[5]==' ':
        twoside(0,0,0,2,0,5,0,0,1)

    elif(a[0]==' 'and a[4]==' ')and a[5]==' ':
        twoside(0,4,0,0,0,5,0,0,1)

    elif(a[2]==' 'and a[3]==' ')and a[4]==' ':
        twoside(0,4,0,2,0,0,0,3,1)

    elif(a[0]==' 'and a[3]==' ')and a[5]==' ':
         twoside(0,0,0,0,0,5,0,3,1)
         
    elif(a[2]==' 'and a[5]==' ')and a[3]==' ':
         twoside(0,0,0,2,0,5,0,3,1)


    elif(a[0]==' 'and a[3]==' '):
         twoside(0,0,0,0,0,0,0,3,1)

    elif(a[0]==' 'and a[4]==' '):
         twoside(0,4,0,0,0,0,0,0,1)

    elif(a[0]==' 'and a[5]==' '):
         twoside(0,0,0,0,0,5,0,0,1)

    elif(a[0]==' 'and a[2]==' '):
         twoside(0,0,0,2,0,0,0,0,1)

    elif(a[3]==' 'and a[4]==' '):
         twoside(0,4,0,0,0,0,0,3,1)

    elif(a[3]==' 'and a[5]==' '):
         twoside(0,0,0,0,0,5,0,3,1)

    elif(a[3]==' 'and a[2]==' '):
         twoside(0,0,0,2,0,0,0,3,1)

    elif(a[4]==' 'and a[5]==' '):
         twoside(0,4,0,0,0,5,0,0,1)

    elif(a[4]==' 'and a[2]==' '):
         twoside(0,4,0,2,0,0,0,0,1)

    elif(a[5]==' 'and a[2]==' '):
         twoside(0,0,0,2,0,5,0,0,1)

    elif a[0]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[0]=a[1]
        a[1]=' '
        text()
        text_input.delete(0.0,END)

    elif a[2]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[2]=a[1]
        a[1]=' '
        text()
        text_input.delete(0.0,END)

    elif a[3]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[3]=a[1]
        a[1]=' '
        text()
        text_input.delete(0.0,END)

    elif a[4]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[4]=a[1]
        a[1]=' '
        text()
        text_input.delete(0.0,END)

    else:
        
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[5]=a[1]
        a[1]=' '
        text()
        text_input.delete(0.0,END)

     
    l=[a[3]+a[4]+'\n',a[4]+a[3]+'\n',a[4]+a[5]+'\n'
       ,a[5]+a[4]+'\n',a[6]+a[7]+'\n',a[7]+a[6]+'\n',a[7]+a[8]+'\n',a[8]+a[7]+'\n'
       ,a[3]+a[6]+'\n',a[6]+a[3]+'\n',a[1]+a[3]+'\n',a[3]+a[1]+'\n',a[4]+a[7]+'\n'
       ,a[7]+a[4]+'\n',a[2]+a[5]+'\n',a[5]+a[2]+'\n',a[5]+a[8]+'\n',a[8]+a[5]+'\n'
       ,a[3]+a[4]+a[5]+'\n',a[5]+a[4]+a[3]+'\n',a[6]+a[7]+a[8]+'\n'
       ,a[8]+a[7]+a[6]+'\n',a[1]+a[3]+a[6]+'\n',a[6]+a[1]+a[3]+'\n'
       ,a[2]+a[5]+a[8]+'\n',a[8]+a[5]+a[2]+'\n',a[2]+a[4]+a[6]+'\n',a[6]+a[4]+a[2]+'\n'
       ,a[1]+a[4]+a[8]+'\n',a[8]+a[4]+a[1]+'\n',
       a[0]+a[4]+'\n',a[4]+a[0]+'\n',a[3]+a[7]+'\n',a[7]+a[3]+'\n',a[4]+a[8]+'\n'
       ,a[8]+a[4]+'\n',a[2]+a[4]+'\n',a[4]+a[2]+'\n',a[4]+a[6]+'\n',a[6]+a[4]+'\n'
       ,a[7]+a[5]+'\n',a[5]+a[7]+'\n'
       ]

    
       
    text_match(l)
    




def text3():

    
    if(a[1]==' 'and a[4]==' ')and a[5]==' ':
        twoside(0,5,1,0,0,0,0,4,2)
    elif a[1]==' ' and a[4]==' ':
        twoside(0,0,1,0,0,0,0,4,2)

    elif a[1]==' ' and a[5]==' ':
        twoside(0,5,1,0,0,0,0,0,2)

    elif a[4]==' ' and a[5]==' ':
        twoside(0,5,0,0,0,0,0,4,2)

    elif a[1]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[1]=a[2]
        a[2]=' '
        text()
        text_input.delete(0.0,END)
        

    elif a[4]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[4]=a[2]
        a[2]=' '
        text()
        text_input.delete(0.0,END)

    else:
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[5]=a[2]
        a[2]=' '
        text()
        text_input.delete(0.0,END)


    
    l=[a[0]+a[1]+'\n',a[1]+a[0]+'\n',a[3]+a[4]+'\n',a[4]+a[3]+'\n',a[4]+a[5]+'\n'
       ,a[5]+a[4]+'\n',a[6]+a[7]+'\n',a[7]+a[6]+'\n',a[7]+a[8]+'\n',a[8]+a[7]+'\n'
       ,a[3]+a[6]+'\n',a[6]+a[3]+'\n',a[1]+a[4]+'\n',a[4]+a[1]+'\n',a[4]+a[7]+'\n'
       ,a[7]+a[4]+'\n',
       a[5]+a[8]+'\n',a[8]+a[5]+'\n',a[1]+a[3]+'\n',a[3]+a[1]+'\n',a[4]+a[6]+'\n'
       ,a[6]+a[4]+'\n',a[5]+a[7]+'\n',a[7]+a[5]+'\n',a[4]+a[8]+'\n',a[8]+a[4]+'\n'
       ,a[0]+a[4]+'\n',a[4]+a[0]+'\n'
       ,a[0]+a[3]+'\n',a[3]+a[0]+'\n'
       ,a[3]+a[4]+a[5]+'\n',a[5]+a[4]+a[3]+'\n',a[6]+a[7]+a[8]+'\n'
       ,a[8]+a[7]+a[6]+'\n',a[1]+a[4]+a[7]+'\n',a[7]+a[4]+a[1]+'\n'
       ,a[0]+a[3]+a[6]+'\n',a[6]+a[3]+a[0]+'\n',a[0]+a[4]+a[8]+'\n',a[8]+a[4]+a[0]+'\n']
       
    text_match(l)
        
    

def text4():




    if (a[6]==' ' and a[7]==' ')and a[4]==' ':
        twoside(0,6,0,4,0,7,0,0,3)

    elif a[6]==' ' and (a[7]==' 'and a[1]==' '):
        twoside(0,6,0,0,0,7,1,0,3)
        

    elif(a[6]==' ' and a[7]==' ')and a[0]==' ':
        twoside(0,6,0,0,0,7,0,0,3)

    elif(a[6]==' ' and a[4]==' ')and a[1]==' ':
        twoside(0,6,0,4,0,0,1,0,3)

    elif(a[6]==' ' and a[4]==' ')and a[0]==' ':
        twoside(0,6,0,4,0,0,0,0,3)

    elif(a[6]==' ' and a[1]==' ')and a[0]==' ':
        twoside(0,6,0,0,0,0,1,0,3)

    elif(a[7]==' 'and a[4]==' ')and a[1]==' ':
        twoside(0,0,0,4,0,7,1,0,3)

    elif(a[7]==' 'and a[4]==' ')and a[0]==' ':
         twoside(0,0,0,4,0,7,0,0,3)
        

    elif(a[7]==' 'and a[1]==' ')and a[0]==' ':
         twoside(0,0,0,0,0,7,1,0,3)

       
    elif(a[4]==' 'and a[1]=='  ')and a[0]==' ':
          twoside(0,0,0,4,0,0,1,0,3)


    elif(a[6]==' 'and a[7]==' '):
         twoside(0,6,0,0,0,7,0,0,3)

    elif(a[6]==' 'and a[4]==' '):
         twoside(0,6,0,4,0,0,0,0,3)

    elif(a[6]==' 'and a[1]==' '):
         twoside(0,6,0,0,0,0,1,0,3)

    elif(a[6]==' 'and a[0]==' '):
         twoside(0,6,0,0,0,0,0,0,3)

    elif(a[7]==' 'and a[4]==' '):
         twoside(0,0,0,4,0,7,0,0,3)

    elif(a[7]==' 'and a[1]==' '):
         twoside(0,0,0,0,0,7,1,0,3)

    elif(a[7]==' 'and a[0]==' '):
         twoside(0,0,0,0,0,7,0,0,3)

    elif(a[4]==' 'and a[1]==' '):
         twoside(0,0,0,4,0,0,1,0,3)

    elif(a[4]==' 'and a[0]==' '):
         twoside(0,0,0,4,0,0,0,0,3)

    elif(a[1]==' 'and a[0]==' '):
         twoside(0,0,0,0,0,0,1,0,3)

    elif a[0]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[0]=a[3]
        a[3]=' '
        text()
        text_input.delete(0.0,END)

    elif a[1]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[1]=a[3]
        a[3]=' '
        text()
        text_input.delete(0.0,END)

    elif a[4]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[4]=a[3]
        a[3]=' '
        text()
        text_input.delete(0.0,END)

    elif a[7]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[7]=a[3]
        a[3]=' '
        text()
        text_input.delete(0.0,END)

    else:
        
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[6]=a[3]
        a[3]=' '
        text()
        text_input.delete(0.0,END)

    l=[a[0]+a[1]+'\n',a[1]+a[0]+'\n',a[1]+a[2]+'\n'
       ,a[2]+a[1]+'\n',a[4]+a[5]+'\n',a[5]+a[4]+'\n',a[7]+a[8]+'\n',a[8]+a[7]+'\n'
       ,a[7]+a[6]+'\n',a[6]+a[7]+'\n',a[1]+a[4]+'\n',a[4]+a[1]+'\n',a[4]+a[7]+'\n'
       ,a[7]+a[4]+'\n',a[2]+a[5]+'\n',a[5]+a[2]+'\n',a[5]+a[8]+'\n',a[8]+a[5]+'\n'
       ,a[0]+a[1]+a[2]+'\n',a[2]+a[1]+a[0]+'\n',a[6]+a[7]+a[8]+'\n'
       ,a[8]+a[7]+a[6]+'\n',a[1]+a[4]+a[7]+'\n',a[7]+a[4]+a[1]+'\n'
       ,a[2]+a[5]+a[8]+'\n',a[8]+a[5]+a[2]+'\n',a[2]+a[4]+a[6]+'\n',a[6]+a[4]+a[2]+'\n'
       ,a[0]+a[4]+a[8]+'\n',a[8]+a[4]+a[0]+'\n',
       a[0]+a[4]+'\n',a[4]+a[0]+'\n',a[1]+a[5]+'\n',a[5]+a[1]+'\n',a[4]+a[6]+'\n'
       ,a[6]+a[4]+'\n',a[5]+a[7]+'\n',a[7]+a[5]+'\n',a[4]+a[2]+'\n',a[2]+a[4]+'\n'
       ,a[4]+a[8]+'\n',a[8]+a[4]+'\n'
       ]

    
       
    text_match(l)
    
    
    


    

def text5():

    if (a[0]==' ' and a[3]==' ')and a[6]==' ':
        twoside(0,0,3,0,0,0,0,6,4)

    elif a[0]==' ' and (a[3]==' 'and a[7]==' '):
        twoside(0,7,3,0,0,0,0,0,4)
        

    elif(a[0]==' ' and a[3]==' ')and a[8]=='  ':
        twoside(0,0,3,0,0,8,0,0,4)

    elif(a[0]==' ' and a[3]==' ')and a[5]==' ':
        twoside(0,0,3,5,0,0,0,0,4)

    elif(a[0]==' ' and a[3]==' ')and a[2]==' ':
        twoside(0,0,3,0,0,0,2,0,4)

    elif(a[0]==' ' and a[3]==' ')and a[1]==' ':
        twoside(1,0,3,0,0,0,0,0,4)

    elif(a[0]==' 'and a[6]==' ')and a[7]==' ':
        twoside(0,7,0,0,0,0,0,6,4)

    elif(a[0]==' 'and a[6]==' ')and a[8]==' ':
         twoside(0,0,0,0,0,8,0,6,4)
        

    elif(a[0]==' 'and a[6]==' ')and a[5]==' ':
         twoside(0,0,0,5,0,0,0,6,4)

       
    elif(a[0]==' 'and a[6]==' ')and a[2]==' ':
        twoside(0,0,0,0,0,0,2,6,4)
        
    elif (a[0]==' ' and a[6]==' ')and a[1]==' ':
         twoside(1,0,0,0,0,0,0,6,4)

    elif a[0]==' ' and (a[7]==' 'and a[8]==' '):
        twoside(0,7,0,0,0,8,0,0,4)
        

    elif(a[0]==' ' and a[7]==' ')and a[5]==' ':
        twoside(0,7,0,5,0,0,0,0,4)

    elif(a[0]==' ' and a[7]==' ')and a[2]==' ':
        twoside(0,7,0,0,0,0,2,0,4)

    elif(a[0]==' ' and a[7]==' ')and a[1]==' ':
        twoside(1,7,0,0,0,0,0,0,4)

    elif(a[0]==' ' and a[8]==' ')and a[5]==' ':
        twoside(0,0,0,5,0,8,0,0,4)

    elif(a[0]==' 'and a[8]==' ')and a[2]=='  ':
        twoside(0,0,0,0,0,8,2,0,4)

    elif(a[0]==' 'and a[8]==' ')and a[1]==' ':
         twoside(1,0,0,0,0,8,0,0,4)
        

    elif(a[0]==' 'and a[5]==' ')and a[2]==' ':
         twoside(0,0,0,5,0,0,2,0,4)

       
    elif(a[0]==' 'and a[5]==' ')and a[1]==' ':
          twoside(1,0,0,5,0,0,0,0,4)

    elif(a[0]==' 'and a[2]==' ')and a[1]==' ':
          twoside(1,0,0,0,0,0,2,0,4)

    elif(a[3]==' ' and a[6]==' ')and a[7]==' ':
        twoside(0,7,3,0,0,0,0,6,4)

    elif(a[3]==' ' and a[6]==' ')and a[8]==' ':
        twoside(0,0,3,0,0,8,0,6,4)

    elif(a[3]==' ' and a[6]==' ')and a[5]==' ':
        twoside(0,0,3,5,0,0,0,6,4)

    elif(a[3]==' ' and a[6]==' ')and a[2]==' ':
        twoside(0,0,3,0,0,0,2,6,4)

    elif(a[3]==' 'and a[6]==' ')and a[1]==' ':
        twoside(1,0,3,0,0,0,0,6,4)
        
    elif(a[3]==' 'and a[7]==' ')and a[8]==' ':
         twoside(0,7,3,0,0,8,0,0,4)

       
    elif(a[3]==' 'and a[7]==' ')and a[5]==' ':
          twoside(0,7,3,5,0,0,0,0,4)

    elif (a[3]==' ' and a[7]==' ')and a[2]==' ':
        twoside(0,7,3,0,0,0,2,0,4)

    elif a[3]==' ' and (a[7]==' 'and a[1]==' '):
        twoside(1,7,3,0,0,0,0,0,4)
        

    elif(a[3]==' ' and a[8]==' ')and a[5]==' ':
        twoside(0,0,3,5,0,8,0,0,4)

    elif(a[3]==' ' and a[8]==' ')and a[2]==' ':
        twoside(0,0,3,0,0,8,2,0,4)

    elif(a[3]==' ' and a[8]==' ')and a[1]==' ':
        twoside(1,0,3,0,0,8,0,0,4)

    elif(a[3]==' ' and a[5]==' ')and a[2]==' ':
        twoside(0,0,3,5,0,0,2,0,4)

    elif(a[3]==' 'and a[5]==' ')and a[1]==' ':
       twoside(1,0,3,5,0,0,0,0,4)

    elif(a[3]==' 'and a[2]==' ')and a[1]==' ':
        twoside(1,0,3,0,0,0,2,0,4)

    elif(a[6]==' 'and a[7]==' ')and a[8]==' ':
         twoside(0,7,0,0,0,8,0,6,4)

    elif (a[6]==' ' and a[7]==' ')and a[5]==' ':
        twoside(0,7,0,5,0,0,0,6,4)

    elif a[6]==' ' and (a[7]==' 'and a[2]==' '):
        twoside(0,7,0,0,0,0,2,6,4)
        

    elif(a[6]==' ' and a[7]==' ')and a[1]==' ':
        twoside(1,7,0,0,0,0,0,6,4)

    elif(a[6]==' ' and a[8]==' ')and a[5]==' ':
        twoside(0,0,0,5,0,8,0,6,4)

    elif(a[6]==' ' and a[8]==' ')and a[2]==' ':
        twoside(0,0,0,0,0,8,2,6,4)

    elif(a[6]==' ' and a[8]==' ')and a[1]==' ':
        twoside(1,0,0,0,0,8,0,6,4)

    elif(a[6]==' 'and a[5]==' ')and a[2]==' ':
        twoside(0,0,0,5,0,0,2,6,4)

    elif(a[6]==' 'and a[5]==' ')and a[1]==' ':
         twoside(1,0,0,5,0,0,0,6,4)
        
    elif(a[6]==' 'and a[2]==' ')and a[1]==' ':
        twoside(1,0,0,0,0,0,2,6,4)

    
    elif(a[7]==' ' and a[8]==' ')and a[5]==' ':
        twoside(0,7,0,5,0,8,0,0,4)

    elif(a[7]==' ' and a[8]==' ')and a[2]==' ':
        twoside(0,7,0,0,0,8,2,0,4)

    elif(a[7]==' ' and a[8]==' ')and a[1]==' ':
        twoside(1,7,0,0,0,8,0,0,4)

    elif(a[7]==' 'and a[5]==' ')and a[2]==' ':
        twoside(0,7,0,5,0,0,2,0,4)

    elif(a[7]==' 'and a[5]==' ')and a[1]==' ':
        twoside(0,7,0,5,0,0,2,0,4)
        
    elif(a[7]==' 'and a[2]==' ')and a[1]==' ':
        twoside(1,7,0,0,0,0,2,0,4)

    elif(a[8]==' 'and a[5]==' ')and a[2]==' ':
         twoside(0,0,0,5,0,8,2,0,4)

    elif(a[8]==' 'and a[5]==' ')and a[1]==' ':
         twoside(1,0,0,5,0,8,0,0,4)
        
    elif(a[8]==' 'and a[2]==' ')and a[1]==' ':
         twoside(1,0,0,0,0,8,2,0,4)

    elif(a[5]==' 'and a[2]==' ')and a[1]==' ':
         twoside(1,0,0,5,0,0,2,0,4)

    elif(a[0]==' 'and a[3]==' '):
         twoside(0,0,3,0,0,0,0,0,4)

    elif(a[0]==' 'and a[6]==' '):
         twoside(0,0,0,0,0,0,0,6,4)

    elif(a[0]==' 'and a[7]==' '):
         twoside(0,7,0,0,0,0,0,0,4)

    elif(a[0]==' 'and a[8]==' '):
         twoside(0,0,0,0,0,8,0,0,4)

    elif(a[0]==' 'and a[5]==' '):
         twoside(0,0,0,5,0,0,0,0,4)

    elif(a[0]==' 'and a[2]==' '):
         twoside(0,0,0,0,0,0,2,0,4)

    elif(a[0]==' 'and a[1]==' '):
         twoside(1,0,0,0,0,0,0,0,4)

    elif(a[3]==' 'and a[6]==' '):
         twoside(0,0,3,0,0,0,0,6,4)

    elif(a[3]==' 'and a[7]==' '):
         twoside(0,7,3,0,0,0,0,0,4)

    elif(a[3]==' 'and a[8]==' '):
         twoside(0,0,3,0,0,8,0,0,4)
         
    elif(a[3]==' 'and a[5]==' '):
         twoside(0,0,3,5,0,0,0,0,4)

    elif(a[3]==' 'and a[2]==' '):
        twoside(0,0,3,0,0,0,2,0,4)

    elif(a[3]==' 'and a[1]==' '):
         twoside(1,0,3,0,0,0,0,0,4)

    elif(a[6]==' 'and a[7]==' '):
         twoside(0,7,0,0,0,0,0,6,4)

    elif(a[6]==' 'and a[8]==' '):
         twoside(0,0,0,0,0,8,0,6,4)

    elif(a[6]==' 'and a[5]==' '):
         twoside(0,0,0,5,0,0,0,6,4)

    elif(a[6]==' 'and a[2]==' '):
         twoside(0,0,0,0,0,0,2,6,4)

    elif(a[6]==' 'and a[1]==' '):
         twoside(1,0,0,0,0,0,0,6,4)

    elif(a[7]==' 'and a[8]==' '):
         twoside(0,7,0,0,0,8,0,0,4)

    elif(a[7]==' 'and a[5]==' '):
          twoside(0,7,0,5,0,0,0,0,4)

    elif(a[7]==' 'and a[2]==' '):
          twoside(0,7,0,0,0,0,2,0,4)

    elif(a[7]==' 'and a[1]==' '):
          twoside(1,7,0,0,0,0,0,0,4)

    elif(a[8]==' 'and a[5]==' '):
          twoside(0,0,0,5,0,8,0,0,4)

    elif(a[8]==' 'and a[2]==' '):
          twoside(0,0,0,0,0,8,2,0,4)

    elif(a[8]==' 'and a[1]==' '):
          twoside(1,0,0,0,0,8,0,0,4)

    elif(a[5]==' 'and a[2]==' '):
          twoside(0,0,0,5,0,0,2,0,4)

    elif(a[5]==' 'and a[1]==' '):
         twoside(1,0,0,5,0,0,0,0,4)

    elif(a[2]==' 'and a[1]==' '):
         twoside(1,0,0,0,0,0,2,0,4)
        
    
    elif a[0]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[0]=a[4]
        a[4]=' '
        text()
        text_input.delete(0.0,END)

    elif a[3]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[3]=a[4]
        a[4]=' '
        text()
        text_input.delete(0.0,END)

    elif a[6]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[6]=a[4]
        a[4]=' '
        text()
        text_input.delete(0.0,END)

    elif a[7]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[7]=a[4]
        a[4]=' '
        text()
        text_input.delete(0.0,END)

    elif a[8]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[8]=a[4]
        a[4]=' '
        text()
        text_input.delete(0.0,END)

    elif a[5]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[5]=a[4]
        a[4]=' '
        text()
        text_input.delete(0.0,END)

    elif a[2]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[2]=a[4]
        a[4]=' '
        text()
        text_input.delete(0.0,END)

    else:
        
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[1]=a[4]
        a[4]=' '
        text()
        text_input.delete(0.0,END)

    l=[a[0]+a[1]+'\n',a[1]+a[0]+'\n',a[1]+a[2]+'\n'
       ,a[2]+a[1]+'\n',a[7]+a[8]+'\n',a[8]+a[7]+'\n'
       ,a[7]+a[6]+'\n',a[6]+a[7]+'\n',a[0]+a[3]+'\n',a[3]+a[0]+'\n',a[3]+a[6]+'\n'
       ,a[6]+a[3]+'\n',a[2]+a[5]+'\n',a[5]+a[2]+'\n',a[5]+a[8]+'\n',a[8]+a[5]+'\n'
       ,a[0]+a[3]+a[6]+'\n',a[6]+a[3]+a[0]+'\n',a[2]+a[5]+a[8]+'\n'
       ,a[8]+a[5]+a[2]+'\n',a[0]+a[1]+a[2]+'\n',a[2]+a[1]+a[0]+'\n'
       ,a[6]+a[7]+a[8]+'\n',a[8]+a[7]+a[6]+'\n',
       a[1]+a[3]+'\n',a[3]+a[1]+'\n',a[7]+a[5]+'\n',a[5]+a[7]+'\n',a[3]+a[7]+'\n'
       ,a[7]+a[3]+'\n',a[5]+a[1]+'\n',a[1]+a[5]+'\n'
          ]

    
       
    text_match(l)
    



    

def text6():

    
    if (a[2]==' ' and a[1]==' ')and a[4]==' ':
        twoside(2,0,4,0,1,0,0,0,5)

    elif a[2]==' ' and (a[1]==' 'and a[7]==' '):
        twoside(2,0,0,0,1,0,0,7,5)
        

    elif(a[2]==' ' and a[1]==' ')and a[8]==' ':
        twoside(2,8,0,0,1,0,0,0,5)

    elif(a[2]==' ' and a[4]==' ')and a[7]==' ':
        twoside(2,0,4,0,0,0,0,7,5)

    elif(a[2]==' ' and a[4]==' ')and a[8]==' ':
        twoside(2,8,4,0,0,0,0,0,5)

    elif(a[2]==' ' and a[7]==' ')and a[8]==' ':
        twoside(2,8,0,0,0,0,0,7,5)

    elif(a[1]==' 'and a[4]==' ')and a[7]==' ':
        twoside(0,0,4,0,1,0,0,7,5)

    elif(a[1]==' 'and a[4]==' ')and a[8]==' ':
         twoside(0,8,4,0,1,0,0,0,5)
        
    elif(a[4]==' 'and a[7]==' ')and a[8]==' ':
         twoside(0,8,4,0,0,0,0,7,5)

    elif(a[1]==' 'and a[7]==' ')and a[8]==' ':
         twoside(0,8,0,0,1,0,0,7,5)

    elif(a[2]==' 'and a[1]==' '):
         twoside(2,0,0,0,1,0,0,0,5)

    elif(a[2]==' 'and a[4]==' '):
          twoside(2,0,4,0,0,0,0,0,5)

    elif(a[2]==' 'and a[7]==' '):
          twoside(2,0,0,0,0,0,0,7,5)

    elif(a[2]==' 'and a[8]==' '):
          twoside(2,8,0,0,0,0,0,0,5)

    elif(a[1]==' 'and a[4]==' '):
          twoside(0,0,4,0,1,0,0,0,5)

    elif(a[1]==' 'and a[7]==' '):
          twoside(0,0,0,0,1,0,0,7,5)

    elif(a[1]==' 'and a[8]==' '):
          twoside(0,8,0,0,1,0,0,0,5)

    elif(a[4]==' 'and a[7]==' '):
          twoside(0,0,4,0,0,0,0,7,5)

    elif(a[4]==' 'and a[8]==' '):
         twoside(0,8,4,0,0,0,0,0,5)

    elif(a[7]==' 'and a[8]==' '):
         twoside(0,8,0,0,0,0,0,7,5)

    
    elif a[2]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[2]=a[5]
        a[5]=' '
        text()
        text_input.delete(0.0,END)

    elif a[1]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[1]=a[5]
        a[5]=' '
        text()
        text_input.delete(0.0,END)

    elif a[4]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[4]=a[5]
        a[5]=' '
        text()
        text_input.delete(0.0,END)

    elif a[7]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[7]=a[5]
        a[5]=' '
        text()
        text_input.delete(0.0,END)

    else:
        
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[8]=a[5]
        a[5]=' '
        text()
        text_input.delete(0.0,END)

    l=[a[0]+a[1]+'\n',a[1]+a[0]+'\n',a[1]+a[2]+'\n'
       ,a[2]+a[1]+'\n',a[4]+a[3]+'\n',a[3]+a[4]+'\n',a[7]+a[8]+'\n',a[8]+a[7]+'\n'
       ,a[7]+a[6]+'\n',a[6]+a[7]+'\n',a[0]+a[3]+'\n',a[3]+a[0]+'\n',a[3]+a[6]+'\n'
       ,a[6]+a[3]+'\n',a[1]+a[4]+'\n',a[4]+a[1]+'\n',a[7]+a[4]+'\n',a[4]+a[7]+'\n'
       ,a[0]+a[1]+a[2]+'\n',a[2]+a[1]+a[0]+'\n',a[6]+a[7]+a[8]+'\n'
       ,a[8]+a[7]+a[6]+'\n',a[0]+a[3]+a[6]+'\n',a[6]+a[3]+a[0]+'\n'
       ,a[1]+a[4]+a[7]+'\n',a[7]+a[4]+a[1]+'\n',a[2]+a[4]+a[6]+'\n',a[6]+a[4]+a[2]+'\n'
       ,a[0]+a[4]+a[8]+'\n',a[8]+a[4]+a[0]+'\n',
       a[1]+a[3]+'\n',a[3]+a[1]+'\n',a[4]+a[6]+'\n',a[6]+a[4]+'\n',a[4]+a[2]+'\n'
       ,a[2]+a[4]+'\n',a[3]+a[7]+'\n',a[7]+a[3]+'\n',a[4]+a[0]+'\n',a[0]+a[4]+'\n'
       ,a[4]+a[8]+'\n',a[8]+a[4]+'\n'
       ]

    
       
    text_match(l)
    
    
     



    

def text7():
    
    if(a[3]==' 'and a[7]==' ')and a[4]==' ':
        twoside(3,0,0,7,0,0,4,0,6)
        
    elif(a[3]==' 'and a[4]==' '):
          twoside(3,0,0,0,0,0,4,0,6)

    elif(a[3]==' 'and a[7]==' '):
          twoside(3,0,0,7,0,0,0,0,6)

    elif(a[4]==' 'and a[7]==' '):
          twoside(3,0,0,7,0,0,4,0,6)    

    elif a[3]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[3]=a[6]
        a[6]=' '
        text()
        text_input.delete(0.0,END)

    elif a[4]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[4]=a[6]
        a[6]=' '
        text()
        text_input.delete(0.0,END)

    else:
        
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[7]=a[6]
        a[6]=' '
        text()
        text_input.delete(0.0,END)

    
    l=[a[1]+a[2]+'\n',a[2]+a[1]+'\n',a[3]+a[4]+'\n',a[4]+a[3]+'\n',a[4]+a[5]+'\n'
       ,a[5]+a[4]+'\n',a[0]+a[1]+'\n',a[1]+a[0]+'\n',a[7]+a[8]+'\n',a[8]+a[7]+'\n'
       ,a[3]+a[0]+'\n',a[0]+a[3]+'\n',a[1]+a[4]+'\n',a[4]+a[1]+'\n',a[4]+a[7]+'\n'
       ,a[7]+a[4]+'\n',a[2]+a[5]+'\n',a[5]+a[2]+'\n',a[5]+a[8]+'\n',a[8]+a[5]+'\n'
     ,a[3]+a[1]+'\n',a[1]+a[3]+'\n',a[4]+a[2]+'\n',a[2]+a[4]+'\n',a[1]+a[5]+'\n'
       ,a[5]+a[1]+'\n',a[4]+a[0]+'\n',a[0]+a[4]+'\n',a[8]+a[4]+'\n',a[4]+a[8]+'\n'
       ,a[5]+a[7]+'\n',a[7]+a[5]+'\n',a[7]+a[3]+'\n',a[3]+a[7]+'\n'
       ,a[0]+a[1]+a[2]+'\n',a[2]+a[1]+a[0]+'\n',a[3]+a[4]+a[5]+'\n'
       ,a[5]+a[4]+a[3]+'\n',a[1]+a[4]+a[7]+'\n',a[7]+a[4]+a[1]+'\n'
       ,a[2]+a[5]+a[8]+'\n',a[8]+a[5]+a[2]+'\n',a[0]+a[4]+a[8]+'\n',a[8]+a[4]+a[0]+'\n']
       
    text_match(l)
    



    

def text8():
    
    if (a[6]==' ' and a[3]==' ')and a[4]==' ':
        twoside(4,0,6,0,3,0,0,0,7)

    elif a[6]==' ' and (a[3]==' 'and a[5]==' '):
        twoside(0,0,6,0,3,0,5,0,7)

    elif(a[6]==' ' and a[3]==' ')and a[8]==' ':
        twoside(0,0,6,8,3,0,0,0,7)

    elif(a[6]==' ' and a[4]==' ')and a[5]==' ':
        twoside(4,0,6,0,0,0,5,0,7)

    elif(a[6]==' ' and a[4]==' ')and a[8]==' ':
        twoside(4,0,6,8,0,0,0,0,7)

    elif(a[6]==' ' and a[5]==' ')and a[8]==' ':
        twoside(0,0,6,8,3,0,5,0,7)

    elif(a[3]==' 'and a[4]==' ')and a[5]==' ':
        twoside(4,0,0,0,3,0,5,0,7)

    elif(a[3]==' 'and a[4]==' ')and a[8]==' ':
        twoside(4,0,0,8,3,0,0,0,7)

    elif(a[3]==' 'and a[5]==' ')and a[8]==' ':
        twoside(0,0,0,8,3,0,5,0,7)
         
    elif(a[4]==' 'and a[5]==' ')and a[8]==' ':
         twoside(4,0,0,8,0,0,5,0,7)

    elif(a[6]==' 'and a[3]==' '):
         twoside(0,0,6,0,3,0,0,0,7)

    elif(a[6]==' 'and a[4]==' '):
         twoside(4,0,6,0,0,0,0,0,7)

    elif(a[6]==' 'and a[5]==' '):
         twoside(0,0,6,0,0,0,5,0,7)

    elif(a[6]==' 'and a[8]==' '):
         twoside(0,0,6,8,0,0,0,0,7)

    elif(a[4]==' 'and a[5]==' '):
         twoside(4,0,0,0,0,0,5,0,7)

    elif(a[4]==' 'and a[8]==' '):
         twoside(4,0,0,8,0,0,0,0,7)

    elif(a[3]==' 'and a[4]==' '):
         twoside(4,0,0,0,3,0,0,0,7)

    elif(a[3]==' 'and a[5]==' '):
         twoside(0,0,0,0,3,0,5,0,7)

    elif(a[3]==' 'and a[8]==' '):
         twoside(0,0,0,8,3,0,0,0,7)

    elif(a[5]==' 'and a[8]==' '):
         twoside(0,0,0,8,0,0,5,0,7)

    elif a[6]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[6]=a[7]
        a[7]=' '
        text()
        text_input.delete(0.0,END)

    elif a[3]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[3]=a[7]
        a[7]=' '
        text()
        text_input.delete(0.0,END)

    elif a[4]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[4]=a[7]
        a[7]=' '
        text()
        text_input.delete(0.0,END)

    elif a[5]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[5]=a[7]
        a[7]=' '
        text()
        text_input.delete(0.0,END)

    else:
        
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[8]=a[7]
        a[7]=' '
        text()
        text_input.delete(0.0,END)

    
    l=[a[1]+a[2]+'\n',a[2]+a[1]+'\n',a[3]+a[4]+'\n',a[4]+a[3]+'\n',a[4]+a[5]+'\n'
       ,a[5]+a[4]+'\n',a[0]+a[1]+'\n',a[1]+a[0]+'\n'
       ,a[3]+a[0]+'\n',a[0]+a[3]+'\n',a[1]+a[4]+'\n',a[4]+a[1]+'\n',a[4]+a[7]+'\n'
       ,a[7]+a[4]+'\n',a[2]+a[5]+'\n',a[5]+a[2]+'\n',a[5]+a[8]+'\n',a[8]+a[5]+'\n'
      ,a[3]+a[1]+'\n',a[1]+a[3]+'\n',a[4]+a[6]+'\n',a[6]+a[4]+'\n',a[1]+a[5]+'\n'
       ,a[5]+a[1]+'\n',a[4]+a[0]+'\n',a[0]+a[4]+'\n',a[8]+a[4]+'\n',a[4]+a[8]+'\n'
       ,a[2]+a[4]+'\n',a[4]+a[2]+'\n'
       ,a[0]+a[1]+a[2]+'\n',a[2]+a[1]+a[0]+'\n',a[3]+a[4]+a[5]+'\n'
       ,a[5]+a[4]+a[3]+'\n',a[0]+a[3]+a[6]+'\n',a[6]+a[3]+a[0]+'\n'
       ,a[2]+a[5]+a[8]+'\n',a[8]+a[5]+a[2]+'\n',a[0]+a[4]+a[8]+'\n',a[8]+a[4]+a[0]+'\n',a[2]+a[4]+a[6]+'\n',a[6]+a[4]+a[2]+'\n']
       
    text_match(l)




    

def text9():

        
    if(a[5]==' 'and a[7]==' ')and a[4]==' ':
          twoside(5,0,7,0,4,0,0,0,8)
        
    elif(a[7]==' 'and a[4]==' '):
          twoside(0,0,7,0,4,0,0,0,8)

    elif(a[7]==' 'and a[5]==' '):
          twoside(5,0,7,0,0,0,0,0,8)

    elif(a[4]==' 'and a[5]==' '):
          twoside(5,0,0,0,4,0,0,0,8)    

    elif a[7]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[7]=a[8]
        a[8]=' '
        text()
        text_input.delete(0.0,END)

    elif a[4]==' ':
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[4]=a[8]
        a[8]=' '
        text()
        text_input.delete(0.0,END)

    else:
        
        canvas.delete('text1','text2','text3','text4','text5','text6','text7','text8','text9')
        a[5]=a[8]
        a[8]=''
        text()
        text_input.delete(0.0,END)


    l=[a[1]+a[2]+'\n',a[2]+a[1]+'\n',a[3]+a[4]+'\n',a[4]+a[3]+'\n',a[4]+a[5]+'\n'
       ,a[5]+a[4]+'\n',a[0]+a[1]+'\n',a[1]+a[0]+'\n',a[7]+a[6]+'\n',a[6]+a[7]+'\n'
       ,a[3]+a[0]+'\n',a[0]+a[3]+'\n',a[1]+a[4]+'\n',a[4]+a[1]+'\n',a[4]+a[7]+'\n'
       ,a[7]+a[4]+'\n',a[2]+a[5]+'\n',a[5]+a[2]+'\n',a[3]+a[6]+'\n',a[6]+a[3]+'\n'
      ,a[3]+a[1]+'\n',a[1]+a[3]+'\n',a[4]+a[6]+'\n',a[6]+a[4]+'\n',a[1]+a[5]+'\n'
       ,a[5]+a[1]+'\n',a[4]+a[0]+'\n',a[0]+a[4]+'\n',a[2]+a[4]+'\n',a[4]+a[2]+'\n'
       ,a[5]+a[7]+'\n',a[7]+a[5]+'\n',a[7]+a[3]+'\n',a[3]+a[7]+'\n'
       ,a[0]+a[1]+a[2]+'\n',a[2]+a[1]+a[0]+'\n',a[3]+a[4]+a[5]+'\n'
       ,a[5]+a[4]+a[3]+'\n',a[1]+a[4]+a[7]+'\n',a[7]+a[4]+a[1]+'\n'
       ,a[0]+a[3]+a[6]+'\n',a[6]+a[3]+a[0]+'\n',a[2]+a[4]+a[6]+'\n',a[6]+a[4]+a[2]+'\n']
       
    text_match(l)
    

    
 


    
root=Tk()
root.title('PUZZLE GAMES')
aniket=StringVar()
global a
a=['A','E',' ','E',' ','S',' ','H','O']
canvas=Canvas(root,width=300,height=300,bg='light blue')
canvas.place(x=350,y=200)
l1=canvas.create_line(0,2,300,2,fill="red",tags="line1",width=5)
l2=canvas.create_line(0,100,300,100,fill="red",tags="line2",width=5)
l3=canvas.create_line(0,200,300,200,fill="red",tags="line3",width=5)
l4=canvas.create_line(0,300,300,300,fill="red",tags="line4",width=5)
l5=canvas.create_line(2,0,2,300,fill="red",tags="line5",width=5)
l6=canvas.create_line(100,0,100,300,fill="red",tags="line6",width=5)
l7=canvas.create_line(200,0,200,300,fill="red",tags="line7",width=5)
l8=canvas.create_line(300,0,300,300,fill="red",tags="line8",width=5)
run=Button(root,text='run',command=text,bg='light blue',fg='red')
run.place(x=350,y=510)
button1=Button(root,text='b1',command=text1,bg='light blue',fg='red')
button1.place(x=350,y=550)
button2=Button(root,text='b2',command=text2,bg='light blue',fg='red')
button2.place(x=400,y=550)
button3=Button(root,text='b3',command=text3,bg='light blue',fg='red')
button3.place(x=440,y=550)
restart=Button(root,text='restart',command=restart,bg='light blue',fg='red')
restart.place(x=400,y=510)
button4=Button(root,text='b4',command=text4,bg='light blue',fg='red')
button4.place(x=480,y=550)
button5=Button(root,text='b5',command=text5,bg='light blue',fg='red')
button5.place(x=520,y=550)
button6=Button(root,text='b6',command=text6,bg='light blue',fg='red')
button6.place(x=560,y=550)
button7=Button(root,text='b7',command=text7,bg='light blue',fg='red')
button7.place(x=600,y=550)
button8=Button(root,text='b8',command=text8,bg='light blue',fg='red')
button8.place(x=640,y=550)
button9=Button(root,text='b9',command=text9,bg='light blue',fg='red')
button9.place(x=680,y=550)
label=Label(root,text='input',font='arial 13 bold',fg='red')
label.place(x=350,y=150)
entry=Entry(root,width=20,bg='light blue',fg='red',textvariable=aniket)
entry.place(x=400,y=150)
text_input=Text(root,width=50,height=5,bg='light blue',fg='red')
text_input.place(x=540,y=100)

            


root.mainloop()
