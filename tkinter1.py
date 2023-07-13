import os
import time

import tkinter
from tkinter import *
root=Tk()
root.title('Word Finder')

def valid(i,j,m,n):
    if(i<0 or i>=m or j<0 or j>=n):
        return FALSE
    else:
        return TRUE
    
def dfs(i,j,vis,word,index,wordsearch,labeltotal,ans):
    
    if(valid(i,j,len(word),len(word[0]))):
        if(vis[i][j]==0):
            vis[i][j]=1
            if(index==len(wordsearch)-1):
                label=labeltotal[i][j]
                label.config(bg="green")
                label.update()
                label.after(3000)
                if(word[i][j]!=wordsearch[index]):
                    label=labeltotal[i][j]
                    label.config(bg="red")
                    label.update()
                    label.after(3000)
                    label.config(bg="white")
                    label.update()
                    label.after(3000)
                    vis[i][j]=0
                
                return word[i][j]==wordsearch[index]
            
            label=labeltotal[i][j]
            label.config(bg="green")
            label.update()
            label.after(3000)
            
            if(word[i][j]==wordsearch[index]):
                ans=(dfs(i+1,j,vis,word,index+1,wordsearch,labeltotal,ans) or dfs(i,j-1,vis,word,index+1,wordsearch,labeltotal,ans) or dfs(i,j+1,vis,word,index+1,wordsearch,labeltotal,ans) or dfs(i-1,j,vis,word,index+1,wordsearch,labeltotal,ans) )
                if(ans==FALSE):
                    label=labeltotal[i][j]
                    label.config(bg="red")
                    label.update()
                    label.after(3000)
                    label.config(bg="white")
                    label.update()
                    label.after(3000)
                    vis[i][j]=0
                return ans
            else:
                vis[i][j]=0
                label=labeltotal[i][j]
                label.config(bg="red")
                label.update()
                label.after(3000)
                label.config(bg="white")
                label.update()
                label.after(3000)
                
                return FALSE
        else:
            return FALSE
        
    else:
        return FALSE
                
            




root.geometry('400x300')

word=[
    ['A','B','X','X','A','B'],
    ['S','F','C','S','B','A'],
    ['A','X','X','X','K','J']
]
wordfinal="ABFXXXSBAXXC"

labeltotal=[]
vis=[]
for i in range(len(word)):
    arr=[]
    arr1=[]
    for j in range(len(word[0])):
        mylabel1=Label(root,text=word[i][j],bg="white",width=5,height=5)
        mylabel1.grid(row=i,column=j,padx=3,pady=3)
        arr.append(mylabel1)
        arr1.append(0)
    labeltotal.append(arr)
    vis.append(arr1)

vis1=vis
a=[]

for i in range(len(word)):
    for j in range(len(word[0])):
        if(word[i][j]==wordfinal[0]):
            a.append([i,j])

ans=FALSE
for i in a:
    ans=dfs(i[0],i[1],vis,word,0,wordfinal,labeltotal,FALSE)
    if(ans==TRUE):
        finallabel=Label(root,text="Success!",bg="green",width=5*len(word[0]),height=5)
        finallabel.grid(row=0,column=len(word[0]),padx=3,pady=3)
        finallabel.update()
        finallabel.after(1000)
        break
    for j in range(len(word)):
        for k in range(len(word[0])):
            vis[j][k]=0
    
if(ans==FALSE):
    finallabel=Label(root,text="Not Found",bg="red",width=5*len(word[0]),height=5)
    finallabel.grid(row=0,column=len(word[0]),padx=3,pady=3)
    finallabel.update()
    finallabel.after(1000)

exit()
root.mainloop()