# from symbol import compound_stmt
import tkinter as ttk
import pandas as pd

model = pd.read_pickle('adm.pickle')

app = ttk.Tk()
app.geometry('600x600')
app.title('Admission Chances')


gre_score = ttk.Variable(app)
ttk.Label(app, text = 'GRE_score', padx=1, pady=15, font=('Arial',14)).grid(row=0, column=0)
ttk.Label(app, text = '(out of 340)', padx=1, pady=15).grid(row=0, column=1)
ttk.Entry(app, textvariable=gre_score, width=14).grid(row=0, column=3)

toefl_score = ttk.Variable(app)
ttk.Label(app, text = 'TOEFL_score', padx=1, pady=15, font=('Arial',14)).grid(row=1, column=0)
ttk.Label(app, text = '(out of 120)', padx=1, pady=15).grid(row=1, column=1)
ttk.Entry(app, textvariable=toefl_score, width=14).grid(row=1, column=3)

univ_rating = ttk.Variable(app)
ttk.Label(app, text = 'University Rating', padx=1, pady=15, font=('Arial',14)).grid(row=2, column=0)
ttk.Label(app, text = '(out of 5)', padx=1, pady=15).grid(row=2, column=1)
ttk.Entry(app, textvariable=univ_rating, width=14).grid(row=2, column=3)

sop = ttk.Variable(app)
ttk.Label(app, text = 'Statement of Purpose', padx=1, pady=15, font=('Arial',14)).grid(row=3, column=0)
ttk.Label(app, text = '(out of 5)', padx=1, pady=15).grid(row=3, column=1)
ttk.Entry(app, textvariable=sop, width=14).grid(row=3, column=3)

lor = ttk.Variable(app)
ttk.Label(app, text = 'Letter of Recommendation', padx=10, pady=15, font=('Arial',14)).grid(row=4, column=0)
ttk.Label(app, text = '(out of 5)', padx=1, pady=15).grid(row=4, column=1)
ttk.Entry(app, textvariable=lor, width=14).grid(row=4, column=3)

cgpa = ttk.Variable(app)
ttk.Label(app, text = 'CGPA', padx=1, pady=15, font=('Arial',14)).grid(row=5, column=0)
ttk.Label(app, text = '(out of 10)', padx=1, pady=15).grid(row=5, column=1)
ttk.Entry(app, textvariable=cgpa, width=14).grid(row=5, column=3)

research = ttk.Variable(app)
ttk.Label(app, text = 'Research', padx=1, pady=15, font=('Arial',14)).grid(row=6, column=0)
ttk.Label(app, text = '(Yes:1 OR No:0)', padx=1, pady=15, font=('Arial',10)).grid(row=6, column=1)
ttk.Entry(app, textvariable=research, width=14).grid(row=6, column=3)


ttk.Label(app, text = '\t\t    ', padx=15, pady=15).grid(row=3, column=2)



def prediction():
    global model
    global query_data
    query_data = {  'GRE Score':[eval(gre_score.get())],
                'TOEFL Score':[eval(toefl_score.get())],
                'University Rating':[eval(univ_rating.get())],
                'SOP':[eval(sop.get())],
                'LOR ':[eval(lor.get())],
                'CGPA':[eval(cgpa.get())],
                'Research':[eval(research.get())]
                }
    if (eval(gre_score.get()) > 340 or eval(gre_score.get()) < 0 or
        eval(toefl_score.get()) > 120 or eval(toefl_score.get()) < 0 or
        eval(univ_rating.get()) > 5 or eval(univ_rating.get()) < 0 or
        eval(sop.get()) > 5 or eval(sop.get()) < 0 or
        eval(lor.get()) > 5 or eval(lor.get()) < 0 or
        eval(cgpa.get()) > 10 or eval(cgpa.get()) < 0 or
        eval(research.get()) > 1 or eval(research.get()) < 0
            ):
            ttk.Label(app, text = '      Invalid Entry!!     \t', padx=15, pady=15, font=('Arial',18), fg='#f00').place(x=190,y=400)


    else:
        chance = model.predict(pd.DataFrame(query_data))
        result.set(round(100*float(chance), 4))
        ttk.Label(app, text = 'Chances of admission', padx=15, pady=15, font=('Arial',18)).place(x=190,y=400)
        ttk.Label(app, textvariable=result, pady=15, font=('Arial',15), fg='#f00').place(x= 270, y=450)
        ttk.Label(app, text = '%', pady=15, font=('Arial',15)).place(x=350,y=450)


ttk.Button(app, text='Predict', command=prediction, font=('Arial',20), bg='#CCCCCC', fg='#000').place(x=260, y=510)

result = ttk.Variable(app)
result.set('0')
ttk.Label(app, text = 'Chances of admission', padx=15, pady=15, font=('Arial',18)).place(x=190,y=400)
""" ttk.Label(app, textvariable=result, pady=15, font=('Arial',15), fg='#f00').place(x= 270, y=450)
ttk.Label(app, text = '%', pady=15, font=('Arial',15)).place(x=350,y=450) """


app.mainloop()