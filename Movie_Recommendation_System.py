

from tkinter import *
import os
import pandas as pd 
import csv
import numpy as np
import matplotlib.pyplot as pt

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import matplotlib.pyplot as pt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
global tkvar2
path="datamovieset.csv"
df=pd.read_csv(path,error_bad_lines=False)
path1="choice.csv"
col_name=['index','title','release date','hero','heroine','director','genre','rating']
df1=pd.read_csv(path1,error_bad_lines=False)
df2=pd.read_csv("choice1.csv",error_bad_lines=False)

def survey():
    global survey_screen
    global root
    #survey_screen = Toplevel(main_screen)
    #survey_screen.title("Survey")
    root=Tk()
    root.title("Survey ")
    root.config(bg="turquoise")
    root.geometry("600x500")
    mainframe1=Frame(root)
    #mainframe1.grid(column=0,row=0,sticky=(N,W,E,S))
    #mainframe1.columnconfigure(0,width=1)
    mainframe1.pack(pady=100,padx=100)
    
    global tkvar
    tkvar =StringVar(root)
    global tkvar1
    tkvar1=StringVar(root)
    global tkvar2
    tkvar2=StringVar(root)
    global ch    
    global ch1
    global ch2
    
    tkvar.set('Select any one')
    Label(mainframe1,text="Select Your favourite Actor",width="300",height="1",bg="turquoise",font=("Calibri", 13)).pack()
    popupMenu=OptionMenu(mainframe1,tkvar,*df['hero'].unique()).pack()
    Label(text="",bg='turquoise').pack()
    tkvar1.set('Select any one')
    Label(mainframe1,text="Select Your favourite Actress",width="300",height="1",bg="turquoise",font=("Calibri", 13)).pack()
    popupMenu=OptionMenu(mainframe1,tkvar1,*df['heroine'].unique()).pack()
    Label(text="",bg='turquoise').pack()
    tkvar2.set('Select any one')
    Label(text="",bg='turquoise').pack()
    Label(mainframe1,text="Select Your favourite Genre",width="300",height="1",bg="turquoise",font=("Calibri", 13)).pack()
    popupMenu=OptionMenu(mainframe1,tkvar2,*df['genre'].unique()).pack()
    

    Label(mainframe1,text="",bg='turquoise',width=300).pack()
    
    Button(mainframe1,text="SUBMIT", height="2", width="30",bg="Deep Pink",command=similarity).pack()    
    #popupMenu.grid(row=2,column=1)
    #tk.Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).grid(row=0) 



def delete_survey_success():
    survey_success_screen.destroy()

def survey2():
    survey_sucess()

def survey_sucess():
    global survey_success_screen
    survey_success_screen = Toplevel(main_screen)
    survey_success_screen.title("Survey Success")
    survey_success_screen.config(bg="turquoise")
    survey_success_screen.geometry("600x500")
    Label(survey_success_screen, text="CLICK ON ANY OF THE METHOD ",font=("calibri", 30),bg="midnight blue",fg="white",width=300).pack()
    #Button(survey_success_screen, text="ok", fg="green",command=resultd).pack()
    Label(survey_success_screen, text="",bg="turquoise").pack()
    Label(survey_success_screen, text="",bg="turquoise").pack()
    
    Button(survey_success_screen, text="CONTENT BASED ", fg="white",command=survey,bg="Deep Pink",height=5,width=30,font=("Calibri", 14,'bold')).pack()
    Label(survey_success_screen, text="",bg="turquoise").pack()
    Button(survey_success_screen, text="COLLABORATIVE FILTERING", fg="white",command=col1,bg="Deep Pink",height=5,width=30,font=("Calibri", 14,'bold')).pack()
    Label(survey_success_screen, text="",bg="turquoise").pack()
'''def resultd():
    global re_success_screen
    re_success_screen = Toplevel(main_screen)
    re_success_screen.title("Success")
    re_success_screen.geometry("400x300")
    Label(re_success_screen, text="").pack()
    Label(re_success_screen, text="").pack()
    
    Button(re_success_screen, text="Content Based", fg="green",command=similarity).pack()
    Label(re_success_screen, text="").pack()
    Button(re_success_screen, text="Collabrative Based", fg="green",command=col).pack()
    Label(re_success_screen, text="").pack()'''
    
    
def similarity():
    global result_success_screen
    result_success_screen = Toplevel(main_screen)
    result_success_screen.title("Success")
    result_success_screen.geometry("600x500")
    result_success_screen.config(bg='turquoise')
    global rows
    global row
    row=[]
    global row_cnt
    rows=[]
    global fields
    fields=[]
    ch=tkvar.get()
    print(ch)
    ch1=tkvar1.get()
    print(ch1)
    ch2=tkvar2.get()
    print(ch2)
    cnt=0
    
    
    
    #while cnt <= len(df):
    #whil
    dff1=pd.read_csv('datamovieset.csv',index_col='genre')
    dff2=pd.read_csv('datamovieset.csv',index_col='hero')
    dff3=pd.read_csv('datamovieset.csv',index_col='heroine')    
    f=dff1.loc[ch2]
    f1=dff3.loc[ch1]
    f2=dff2.loc[ch]
    #print(f)
    #print(f1)
    #print(f2)
    #s1=pd.concat(f,sort=True)
    #print("\nTop rated Movies According to genre::\n")
    #s1=f.sort_values(by=f['ratings'],ascending=False).head(3)
    #print(s1)
    #print("\nTop rated Movies According to hero::\n")
    #s2=f2.sort_values(by=f2['ratings'],ascending=False).head(3)
    #print(s2)
    #print("\nTop rated Movies According to heroine::\n")
    #s3=f1.sort_values(by=f1['ratings'],ascending=False).head(3)
    #print(s3)
    
    r=[f,f1,f2]
    #r=[s1,s2,s3]
    result=pd.concat(r,sort=True)
    #printnullv(result)
    result1=result.fillna(0)
    
    #print(result.sort_values(by=result['ratings'],ascending=False))
    #print(result['index'],result['title'],result['release date'],result['hero'],result['heroine'],result['director'],result['genre'],result['ratings'])
    print(result1)#['title'],result['ratings'])
    #r=[s1,s2,s3]
    #result=pd.concat(r,sort=true)
    #print(result)
    '''row = [ch,ch1,ch2]
    with open('choice.csv', 'r') as readFile:
        with open('choice.csv', 'a')as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            csvFile.close()
            readFile.close()'''
    
    
    '''with open('choice1.csv', 'r') as readFile1:
        with open('choice1.csv', 'a')as csvFile1:
            writer = csv.writer(csvFile1)
            
            writer.writerow(s1)
            csvFile1.close()
            readFile1.close()'''
    #result=pd.concat(result,sort=True)
    
    #resultt=result1.sort_values(by='ratings',ascending=False)
    m_name=result1['title']
    rate=result1['ratings'].astype(int)
    col=['green','pink','blue','yellow','red','blue','purple']
    Label(result_success_screen,text="",height=5,bg="turquoise").pack()
    figure2=Figure(figsize=(5,4),dpi=100)
    c=Canvas(result_success_screen,height=400,width=400)
    sp=figure2.add_subplot(111)
    sp.pie(rate,labels=m_name,colors=col,startangle=140)
    pie2=FigureCanvasTkAgg(figure2,result_success_screen)
    pie2.get_tk_widget().pack()
    c.pack()
    Label(c,text="",height=5,bg="turquoise").pack()


    #pt.pie(rate,labels=m_name,colors=col,startangle=140).pack()
    
    
    #print(df1)
    
    #row = [ch, ch1,ch2]
    #with open('choice.csv', 'r') as readFile:
     #   reader = csv.reader(readFile)
      #  lines = list(reader)
       # lines = row
        #with open('choice.csv', 'w') as writeFile:
         #   writer = csv.writer(writeFile)
          #  writer.writerows(lines)
           # readFile.close()
            #writeFile.close()
    #row=[ch,ch1,ch2]
    #with open('records.csv','')
    #print(ch)
    #row =StringVar(root)
    #read1=path.reader(df)
    #for row in df:
    #if (df['genre']==ch).any():
        #global r
     #   print(df)
            #print()
        #Label(survey_success_screen,text=r,width="150",height="1",fg="blue").pack()
    


def col1():
    global col1_success_screen
    global tkvar4
    
    global root1
    #survey_screen = Toplevel(main_screen)
    #survey_screen.title("Survey")
    root1=Tk()
    root1.title("Success ")
    root1.config(bg="turquoise")
    root1.geometry("600x500")
    mainframe2=Frame(root1)
    #mainframe1.grid(column=0,row=0,sticky=(N,W,E,S))
    #mainframe1.columnconfigure(0,width=1)
    mainframe2.pack(pady=100,padx=100)
    
    
    #global tkvar
    #tkvar =StringVar(root)
   
    
    tkvar4=StringVar(root1)
    #col1_success_screen = Toplevel(main_screen)
    #col1_success_screen.title("Success")
    #col1_success_screen.config(bg="turquoise")
    #col1_success_screen.geometry("600x500")
    tkvar4.set('Select any one')
    Label(mainframe2,text="Select one of your favorite movie",width="300",height="5",fg="white",bg="midnight blue",font=("Calibri", 13)).pack()
    popupMenu=OptionMenu(mainframe2,tkvar4,*df['title']).pack()
    
    Button(mainframe2,text="SUBMIT", height="3", width="30",bg="red",command=col).pack() 
    
def col():
    
    global col_success_screen
    col_success_screen = Toplevel(main_screen)
    col_success_screen.title("Success")
    col_success_screen.geometry("600x500")
    col_success_screen.config(bg="turquoise")
   
    
    '''i=0
    print("Top 5 similar movies to "+movie_user_likes+" are:")
    for element in sorted_similar_movies:
        dp=get_index_from_title(movie_user_likes)
        pd1=get_title_from_index(dp)
        #Label(col_success_screen, text=pd1, fg="red").pack()
        #print(pd1)
        #dff33=pd.read_csv('datamovieset.csv',index_col='index')    
        #f=dff33.loc[pd1]
        #Label(col_success_screen, text=f['title'], fg="red").pack()
        
        i=i+1
        if i>=5:
            break

    '''
    features = ['hero','genre','title']

    df[features].head(3)


    for feature in features:
        df[feature] = df[feature].fillna('')


    def combine_features(row):
        return row['title']+" "+row["hero"]+" "+row["genre"]

    df["combined_features"] = df.apply(combine_features,axis=1)

    df.head(3)


    count_matrix = CountVectorizer().fit_transform(df["combined_features"])
    

    cosine_sim = cosine_similarity(count_matrix)


    print(cosine_sim)

    cosine_sim.shape

    def get_title_from_index(index):
        return df[df['index'] == index]["title"].values[0]

#Helper function to get the index from the title

    def get_index_from_title(title):
        return df[df['title'] == title]["index"].values[0]


#def get_title_from_index1(index):
#  return df[df['index'] == index]["genre"].values[0]




    movie_user_likes =tkvar4.get()

    movie_index = get_index_from_title(movie_user_likes)


    similar_movies =  list(enumerate(cosine_sim[movie_index]))



#Sort the list of similar movies according to the similarity scores in descending order
#Since the most similar movie is itself, we will discard the first element after sorting.
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)#.all()#[1:]#.all()

#Print the sorted similar movies to the movie the user like
# The tuples are in the form (movie_index, similarity value)
    print(sorted_similar_movies)

    i=0
    print("Top 5 similar movies to "+movie_user_likes+" are:")
    print(sorted_similar_movies)
    Label(col_success_screen, text="RECOMMENDED MOVIES ARE :",bg="turquoise", fg="Black",width=300,height=5,font=("calibari",14)).pack()

    for i in range( len(sorted_similar_movies)):
        #print('Movie title:')
        dpp1=get_title_from_index(sorted_similar_movies[i][0])
        d=sorted_similar_movies[i][0] 
        print(d)
        dff33=pd.read_csv('datamovieset.csv',index_col='index')    
        f=dff33.loc[d]
        #Label(col_success_screen, text="Top 5 similar movies to "+movie_user_likes+" are:", fg="red").pack()
        Label(col_success_screen, text=f['title'], fg="white",bg="midnight blue",width=30,height=3).pack()
        
      
        
        '''
        m_name=f['title']
        rate=f['ratings'].astype(int)
        col=['green','pink','blue','yellow','red','blue','purple']
    
        figure2=Figure(figsize=(5,4),dpi=100)
        c=Canvas(col_success_screen,height=800,width=800)
        sp=figure2.add_subplot(111)
        sp.pie(rate,labels=m_name,colors=col,startangle=140)
        pie2=FigureCanvasTkAgg(figure2,col_success_screen)
        pie2.get_tk_widget().pack()
        c.pack()
        '''
        i=i+1
        if i>=5:
            break
    

    #Button(result_success_screen, text="collabrative", fg="green",command=col).pack()
    
    
    
    
        #re1=get_title_from_index1(d)
        #Label(col_success_screen, text=re1, fg="red").pack()
        
        #Label(col_success_screen, text=d, fg="green").pack()
    '''
    dff33=pd.read_csv('datamovieset.csv',index_col='genre')    
        f=dff33.loc[re1]'''
        
        #Label(col_success_screen, text=f['title'], fg="red").pack()
        #print(f)    
        #print(f['title'])
        
    # Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.config(bg="turquoise")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", fg="white",bg="midnight blue",width=300,height=3).pack()
    Label(register_screen, text="",bg="turquoise").pack()
    username_lable = Label(register_screen, text="Username * ",bg="turquoise")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ",bg="turquoise")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="",bg="turquoise").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="Deep Pink", command = register_user).pack()
 
 
# Designing window for login 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.config(bg="turquoise")
    Label(login_screen, text="Please enter details below to login",fg="white",bg="midnight blue",width=300,height=3).pack()
    Label(login_screen, text="",bg="turquoise").pack()
 
    #username_verify=tkinter_variable(master=none)
    #var.set("kavita")
    #password_verify=tkinter_variable(master=none)
    #var.set("123")
    global username_verify
    global password_verify
 
    username_verify = StringVar("")
    password_verify = StringVar("")
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username ",bg="turquoise").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="",bg="turquoise").pack()
    Label(login_screen, text="Password ",bg="turquoise").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="",bg="turquoise").pack()
    Button(login_screen, text="Login", width=10, height=1,bg="Deep Pink", command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            #login_sucess()
            survey2()
        else:
            password_not_recognised()
 
    else:
        user_not_found()

# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
    
def survey_form():
        survey()

def delete_survey_sucess():
    survey_form.destroy()
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", fg="green",command=survey_form).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 

# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x500")
    main_screen.title("Account Login")
    main_screen.config(bg='turquoise')
    Label(text="MOVIE RECOMMENDATION SYSTEM", bg="midnight blue", width="300", height="6",fg='white', font=("Calibri", 26)).pack()
    #Label(text="Welcome to  movie recommendation system!!!", bg="midnight blue", width="300", height="2",fg='white', font=("Calibri", 22)).pack()
    Label(text="login to the system and if you are new then register yourself", bg="turquoise", width="300", height="2",fg='black', font=("Calibri", 22)).pack()
    Label(text="",bg='turquoise').pack()
    Button(text="LOGIN", height="6", width="30", command = login,bg='Deep Pink',fg='white',font=("Calibri", 14,'bold')).pack()
    Label(text="",bg='turquoise').pack()
    Button(text="REGISTER", height="6", width="30", command=register,fg='white',bg='Deep Pink',font=("Calibri", 14,'bold')).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
