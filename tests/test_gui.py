from pathlib import Path
import sys
import tkinter as tk
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


class GuiTests(unittest.TestCase):
    def setUp(self):
        from tank_gui import App
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = App(self.root)

    def tearDown(self):
        self.root.update()
        self.root.destroy()

    def test_calculate_edit_and_clear(self):
        app = self.app
        for variable, value in zip(app.values, ('1000', '100', '10', '20', '30', '40')):
            variable.set(value)
        app.calculate_button.invoke()
        rows = app.table.get_children()
        self.assertEqual(len(rows), 6)
        self.assertEqual(app.table.item(rows[-1], 'values')[1], '1,200.00')
        app.values[0].set('2000')
        self.assertEqual(app.table.get_children(), ())
        app.clear_button.invoke()
        self.assertEqual([value.get() for value in app.values], [''] + ['0'] * 5)

    def test_invalid_fields_clear_the_table(self):
        for value in ('', 'bad', 'nan', 'inf', '-1'):
            self.app.values[0].set('1000')
            self.app.calculate()
            self.app.values[0].set(value)
            self.app.calculate()
            with self.subTest(value=value):
                self.assertEqual(self.app.table.get_children(), ())
                self.assertNotEqual(self.app.error.get(), '')

    def test_final_stage_is_visible_at_default_size(self):
        self.app.values[0].set('3000')
        self.app.calculate()
        self.root.deiconify()
        self.root.update()
        last = self.app.table.get_children()[-1]
        bounds = self.app.table.bbox(last)
        self.assertTrue(bounds, 'Final DD-4 stage must be visible')
        self.assertLessEqual(bounds[1] + bounds[3], self.app.table.winfo_height())


if __name__ == '__main__':
    unittest.main()
