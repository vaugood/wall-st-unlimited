import tkinter as tk
import wallst as ws

area_statements = []

def runIt():
    lbox.delete(0, tk.END)
    all_statements = ''
    ticker = entry.get()
    data = ws.main(ticker)
    details.config(text=f"{data[0]} -- {data[1]}")
    areas = set([i['area'] for i in data[2]])
    report.config(state=tk.NORMAL)
    report.delete('1.0', tk.END)

    for area in areas:
        lbox.insert(tk.END, area)
        i_area_statement = ''
        for i in data[2]:
            if i['area']==area:
                i_area_statement += f"{i['title']}\n{i['description']}\n\n"
        all_statements += i_area_statement
        area_statement = {'area':area, 'statement':i_area_statement}
        area_statements.append(area_statement)
    report.insert(tk.END, all_statements)


def areaStatement(*args):
    idxs = lbox.curselection()
    if idxs:
        index = idxs[0]
        statements = area_statements[index]
        statement = statements.get('statement','')
        report.config(state=tk.NORMAL)
        report.delete('1.0', tk.END)
        report.insert(tk.END, statement)
        report.config(state=tk.DISABLED)


def showAll():
    lbox.selection_clear(0, tk.END)
    all_statements = ''
    report.config(state=tk.NORMAL)
    report.delete('1.0', tk.END)
    for area_statement in area_statements:
        area_statement = area_statement.get('statement','')
        all_statements += f'{area_statement}'
        report.insert(tk.END, all_statements)
    report.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Wall Street Unlimited")

label = tk.Label(app, text="Ticker:")
label.grid(row=0, column=0, sticky="e")

entry = tk.Entry(app)
entry.grid(row=0, column=1, sticky='w')

run_button = tk.Button(app, text='Get Data', command=runIt, width=20)
run_button.grid(row=1, columnspan=2, padx=5, pady=5)

details = tk.Label(app, text='Supported Search Formats:\n"INTC", "Intel", "NasdaqGS:INTC"')
details.grid(row=2, column=0, columnspan=2)

show_all_button = tk.Button(app, text='Show All', command=showAll, width=20)
show_all_button.grid(row=1, column=3, rowspan=2, columnspan=2)

areas_listbox = tk.StringVar()
lbox_scrollbar = tk.Scrollbar(app)
lbox_scrollbar.grid(row=3, column=4, rowspan=4, sticky="ns")
lbox = tk.Listbox(app, listvariable=areas_listbox, height=5, yscrollcommand=lbox_scrollbar.set)
lbox.grid(row=3, column=3, sticky="news")
lbox.bind('<<ListboxSelect>>', areaStatement)

report_scrollbar = tk.Scrollbar(app)
report_scrollbar.grid(row=3, column=2, sticky="ns")
report = tk.Text(app, wrap=tk.WORD, height=40, width=80, yscrollcommand=report_scrollbar.set)
report.grid(row=3, column=0, columnspan=2,padx=5,pady=5,sticky="w")
report.config(state=tk.DISABLED)

app.mainloop()