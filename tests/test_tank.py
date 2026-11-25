import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


class TankTests(unittest.TestCase):
    def test_stages_preserve_loadout_addition_and_calibration(self):
        from tank_gui import calculate_stages
        stages = calculate_stages(1000, 100, [10, 20, 30, 40])
        self.assertEqual([volume for volume, _ in stages], [1000, 1100, 1110, 1130, 1160, 1200])
        for volume, height in stages:
            self.assertAlmostEqual(height, volume / 4.1404 - 491)

    def test_zero_values_keep_all_stages(self):
        from tank_gui import calculate_stages
        self.assertEqual(calculate_stages(0, 0, [0, 0, 0, 0]), [(0, -491)] * 6)

    def test_invalid_values_are_rejected(self):
        from tank_gui import calculate_stages
        for value in (-1, math.nan, math.inf, -math.inf):
            for position in range(6):
                values = [100, 0, 0, 0, 0, 0]
                values[position] = value
                with self.subTest(value=value, position=position), self.assertRaises(ValueError):
                    calculate_stages(values[0], values[1], values[2:])

    def test_wrong_load_count_is_rejected(self):
        from tank_gui import calculate_stages
        with self.assertRaises(ValueError):
            calculate_stages(100, 0, [1, 2])

    def test_overflow_is_rejected(self):
        from tank_gui import calculate_stages
        with self.assertRaises(ValueError):
            calculate_stages(1e308, 1e308, [0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
