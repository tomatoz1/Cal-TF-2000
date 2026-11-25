"""Windows form preserving the original TF2000-01 arithmetic."""
import math
import tkinter as tk
from tkinter import ttk


def calculate_stages(start, loadout, loads):
    if len(loads) != 4:
        raise ValueError('Provide four DD load-in values.')
    values = [start, loadout, *loads]
    if any(not math.isfinite(value) or value < 0 for value in values):
        raise ValueError('กรอกปริมาตรเป็นตัวเลขตั้งแต่ 0 ขึ้นไป / finite, nonnegative volumes only.')
    stages = []
    volume = 0
    for value in values:
        volume += value
        if not math.isfinite(volume):
            raise ValueError('ค่าปริมาตรมากเกินไป / volume is too large.')
        stages.append((volume, volume / 4.1404 - 491))
    return stages


class App:
    LABELS = ('ยอดเริ่มต้น / Starting volume', 'Load out (+)', 'DD-1 load in', 'DD-2 load in', 'DD-3 load in', 'DD-4 load in')
    STAGES = ('เริ่มต้น / Start', 'หลัง Load out (+)', 'หลัง DD-1', 'หลัง DD-2', 'หลัง DD-3', 'หลัง DD-4')

    def __init__(self, root):
        self.root = root
        root.title('Tank Farm TF2000-01')
        root.geometry('820x790')
        root.minsize(760, 700)
        root.configure(background='#f3f6fa')
        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure('.', font=('Tahoma', 11), background='#f3f6fa')
        style.configure('Title.TLabel', font=('Tahoma', 23, 'bold'), foreground='#173052')
        style.configure('Muted.TLabel', foreground='#53647a')
        style.configure('Error.TLabel', foreground='#b42318')
        style.configure('Accent.TButton', padding=(20, 10), background='#204f88', foreground='white')
        style.configure('TEntry', padding=7)
        style.configure('Treeview', rowheight=30, background='white', fieldbackground='white')
        style.configure('Treeview.Heading', font=('Tahoma', 10, 'bold'), padding=8)
        self.values = [tk.StringVar(value='')] + [tk.StringVar(value='0') for _ in range(5)]
        self.error = tk.StringVar()
        page = ttk.Frame(root, padding=28)
        page.pack(fill='both', expand=True)
        page.columnconfigure(1, weight=1)
        ttk.Label(page, text='Tank Farm TF2000-01', style='Title.TLabel').grid(row=0, column=0, columnspan=2, sticky='w')
        ttk.Label(page, text='คำนวณปริมาตรและระดับน้ำ • หน่วยปริมาตร bbl', style='Muted.TLabel').grid(row=1, column=0, columnspan=2, sticky='w', pady=(6, 16))
        self.entries = []
        for index, (label, variable) in enumerate(zip(self.LABELS, self.values)):
            ttk.Label(page, text=label).grid(row=index + 2, column=0, sticky='w', padx=(0, 22), pady=4)
            entry = ttk.Entry(page, textvariable=variable)
            entry.grid(row=index + 2, column=1, sticky='ew', pady=4)
            self.entries.append(entry)
            variable.trace_add('write', self.invalidate)
        buttons = ttk.Frame(page)
        buttons.grid(row=8, column=0, columnspan=2, sticky='w', pady=(16, 12))
        self.calculate_button = ttk.Button(buttons, text='คำนวณ / Calculate', command=self.calculate, style='Accent.TButton')
        self.calculate_button.pack(side='left')
        self.clear_button = ttk.Button(buttons, text='ล้างค่า / Clear', command=self.clear, padding=(16, 10))
        self.clear_button.pack(side='left', padx=10)
        ttk.Label(page, textvariable=self.error, style='Error.TLabel', wraplength=720).grid(row=9, column=0, columnspan=2, sticky='w')
        table_frame = ttk.Frame(page)
        table_frame.grid(row=10, column=0, columnspan=2, sticky='nsew', pady=(8, 12))
        self.table = ttk.Treeview(table_frame, columns=('stage', 'volume', 'height'), show='headings', height=6, selectmode='none')
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        self.table.pack(side='left', fill='both', expand=True)
        for column, heading, width in (('stage', 'ขั้นตอน / Stage', 270), ('volume', 'ปริมาตร (bbl)', 190), ('height', 'ระดับ (cm)', 190)):
            self.table.heading(column, text=heading)
            self.table.column(column, width=width, minwidth=100, anchor='w' if column == 'stage' else 'e')
        page.rowconfigure(10, weight=1)
        ttk.Label(page, text='Load out นำไปบวกตามระบบเดิม • ใส่ 0 เมื่อไม่มีรายการ', style='Muted.TLabel').grid(row=11, column=0, columnspan=2, sticky='w')
        ttk.Label(page, text='สูตรระดับเดิม: ปริมาตร ÷ 4.1404 − 491 cm', style='Muted.TLabel').grid(row=12, column=0, columnspan=2, sticky='w', pady=(4, 0))
        self.entries[0].focus_set()
        root.bind('<Return>', lambda event: self.calculate())

    def invalidate(self, *_):
        if hasattr(self, 'table'):
            self.table.delete(*self.table.get_children())
        self.error.set('')

    def calculate(self):
        self.invalidate()
        try:
            numbers = []
            for index, variable in enumerate(self.values):
                try:
                    numbers.append(float(variable.get().strip()))
                except ValueError:
                    self.entries[index].focus_set()
                    raise ValueError(f'{self.LABELS[index]}: กรุณากรอกตัวเลข / enter a number.') from None
            stages = calculate_stages(numbers[0], numbers[1], numbers[2:])
        except ValueError as error:
            self.error.set(str(error))
            return
        for label, (volume, height) in zip(self.STAGES, stages):
            self.table.insert('', 'end', values=(label, f'{volume:,.2f}', f'{height:,.2f}'))

    def clear(self):
        for index, variable in enumerate(self.values):
            variable.set('' if index == 0 else '0')
        self.invalidate()
        self.entries[0].focus_set()


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
