import solution
import unittest


class TestNakedTwins(unittest.TestCase):
    before_naked_twins_1 = {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1',
                            'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8',
                            'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3',
                            'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8',
                            'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23',
                            'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
                            'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237',
                            'A5': '9', 'A4': '2357', 'A7': '27', 'A6': '257',
                            'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579',
                            'C7': '9', 'C6': '6', 'C5': '37', 'C4': '4',
                            'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6',
                            'D9': '6', 'H8': '2', 'F6': '125', 'A9': '8',
                            'G4': '9', 'A8': '6', 'E7': '345', 'E3': '379',
                            'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235',
                            'F5': '8', 'E2': '37', 'F7': '35', 'F8': '9',
                            'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9',
                            'H4': '17', 'D3': '2379', 'B4': '27', 'B5': '1',
                            'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9',
                            'B2': '5', 'B3': '6', 'D6': '279', 'D7': '34',
                            'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4',
                            'D1': '5'}
    possible_solutions_1 = [
                            {'G7': '6', 'G6': '3', 'G5': '2', 'G4': '9',
                             'G3': '1', 'G2': '8', 'G1': '7', 'G9': '5',
                             'G8': '4', 'C9': '1', 'C8': '5', 'C3': '8',
                             'C2': '237', 'C1': '23', 'C7': '9', 'C6': '6',
                             'C5': '37', 'A4': '2357', 'A9': '8', 'A8': '6',
                             'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235',
                             'F5': '8', 'F6': '125', 'F7': '35', 'F8': '9',
                             'F9': '7', 'B4': '27', 'B5': '1', 'B6': '8',
                             'B7': '27', 'E9': '2', 'B1': '9', 'B2': '5',
                             'B3': '6', 'C4': '4', 'B8': '3', 'B9': '4',
                             'I9': '9', 'I8': '7', 'I1': '23', 'I3': '23',
                             'I2': '6', 'I5': '5', 'I4': '8', 'I7': '1',
                             'I6': '4', 'A1': '1', 'A3': '4', 'A2': '237',
                             'A5': '9', 'E8': '1', 'A7': '27', 'A6': '257',
                             'E5': '347', 'E4': '6', 'E7': '345', 'E6': '579',
                             'E1': '8', 'E3': '79', 'E2': '37', 'H8': '2',
                             'H9': '3', 'H2': '9', 'H3': '5', 'H1': '4',
                             'H6': '17', 'H7': '8', 'H4': '17', 'H5': '6',
                             'D8': '8', 'D9': '6', 'D6': '279', 'D7': '34',
                             'D4': '237', 'D5': '347', 'D2': '1', 'D3': '79',
                             'D1': '5'},
                            {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1',
                             'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8',
                             'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3',
                             'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8',
                             'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23',
                             'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
                             'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237',
                             'A5': '9', 'A4': '2357', 'A7': '27', 'A6': '257',
                             'C3': '8', 'C2': '237', 'C1': '23', 'E6': '579',
                             'C7': '9', 'C6': '6', 'C5': '37', 'C4': '4',
                             'I9': '9', 'D8': '8', 'I8': '7', 'E4': '6',
                             'D9': '6', 'H8': '2', 'F6': '125', 'A9': '8',
                             'G4': '9', 'A8': '6', 'E7': '345', 'E3': '79',
                             'F1': '6', 'F2': '4', 'F3': '23', 'F4': '1235',
                             'F5': '8', 'E2': '3', 'F7': '35', 'F8': '9',
                             'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9',
                             'H4': '17', 'D3': '79', 'B4': '27', 'B5': '1',
                             'B6': '8', 'B7': '27', 'E9': '2', 'B1': '9',
                             'B2': '5', 'B3': '6', 'D6': '279', 'D7': '34',
                             'D4': '237', 'D5': '347', 'B8': '3', 'B9': '4',
                             'D1': '5'}
        ]

    before_naked_twins_2 = {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6',
                            'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9',
                            'A9': '1', 'B1': '6', 'B2': '9', 'B3': '8',
                            'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237',
                            'B8': '5', 'B9': '237', 'C1': '23', 'C2': '5',
                            'C3': '1', 'C4': '23', 'C5': '379', 'C6': '2379',
                            'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
                            'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6',
                            'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357',
                            'E1': '5', 'E2': '6', 'E3': '2', 'E4': '8',
                            'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1',
                            'E9': '9', 'F1': '4', 'F2': '17', 'F3': '3',
                            'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6',
                            'F8': '8', 'F9': '257', 'G1': '1', 'G2': '8',
                            'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34',
                            'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
                            'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1',
                            'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6',
                            'I1': '9', 'I2': '3', 'I3': '5', 'I4': '7',
                            'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4',
                            'I9': '8'}
    possible_solutions_2 = [
                            {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6',
                             'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9',
                             'A9': '1', 'B1': '6', 'B2': '9', 'B3': '8',
                             'B4': '4', 'B5': '37', 'B6': '1', 'B7': '237',
                             'B8': '5', 'B9': '237', 'C1': '23', 'C2': '5',
                             'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79',
                             'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
                             'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6',
                             'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357',
                             'E1': '5', 'E2': '6', 'E3': '2', 'E4': '8',
                             'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1',
                             'E9': '9', 'F1': '4', 'F2': '17', 'F3': '3',
                             'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6',
                             'F8': '8', 'F9': '257', 'G1': '1', 'G2': '8',
                             'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34',
                             'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
                             'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1',
                             'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6',
                             'I1': '9', 'I2': '3', 'I3': '5', 'I4': '7',
                             'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4',
                             'I9': '8'},
                            {'A1': '23', 'A2': '4', 'A3': '7', 'A4': '6',
                             'A5': '8', 'A6': '5', 'A7': '23', 'A8': '9',
                             'A9': '1', 'B1': '6', 'B2': '9', 'B3': '8',
                             'B4': '4', 'B5': '3', 'B6': '1', 'B7': '237',
                             'B8': '5', 'B9': '237', 'C1': '23', 'C2': '5',
                             'C3': '1', 'C4': '23', 'C5': '79', 'C6': '79',
                             'C7': '8', 'C8': '6', 'C9': '4', 'D1': '8',
                             'D2': '17', 'D3': '9', 'D4': '1235', 'D5': '6',
                             'D6': '237', 'D7': '4', 'D8': '27', 'D9': '2357',
                             'E1': '5', 'E2': '6', 'E3': '2', 'E4': '8',
                             'E5': '347', 'E6': '347', 'E7': '37', 'E8': '1',
                             'E9': '9', 'F1': '4', 'F2': '17', 'F3': '3',
                             'F4': '125', 'F5': '579', 'F6': '279', 'F7': '6',
                             'F8': '8', 'F9': '257', 'G1': '1', 'G2': '8',
                             'G3': '6', 'G4': '35', 'G5': '345', 'G6': '34',
                             'G7': '9', 'G8': '27', 'G9': '27', 'H1': '7',
                             'H2': '2', 'H3': '4', 'H4': '9', 'H5': '1',
                             'H6': '8', 'H7': '5', 'H8': '3', 'H9': '6',
                             'I1': '9', 'I2': '3', 'I3': '5', 'I4': '7',
                             'I5': '2', 'I6': '6', 'I7': '1', 'I8': '4',
                             'I9': '8'}
    ]

    def test_naked_twins(self):
        s_err = 'Your naked_twins function produced an unexpected board.'
        self.assertTrue(solution.naked_twins(self.before_naked_twins_1) in
                        self.possible_solutions_1, s_err)

    def test_naked_twins2(self):
        s_err = 'Your naked_twins function produced an unexpected board.'
        self.assertTrue(solution.naked_twins(self.before_naked_twins_2) in
                        self.possible_solutions_2, s_err)


class TestDiagonalSudoku(unittest.TestCase):
    diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4'
    diagonal_grid += '....8....52.............3'
    solved_diag_sudoku = {'G7': '8', 'G6': '9', 'G5': '7', 'G4': '3',
                          'G3': '2', 'G2': '4', 'G1': '6', 'G9': '5',
                          'G8': '1', 'C9': '6', 'C8': '7', 'C3': '1',
                          'C2': '9', 'C1': '4', 'C7': '5', 'C6': '3',
                          'C5': '2', 'C4': '8', 'E5': '9', 'E4': '1',
                          'F1': '1', 'F2': '2', 'F3': '9', 'F4': '6',
                          'F5': '5', 'F6': '7', 'F7': '4', 'F8': '3',
                          'F9': '8', 'B4': '7', 'B5': '1', 'B6': '6',
                          'B7': '2', 'B1': '8', 'B2': '5', 'B3': '3',
                          'B8': '4', 'B9': '9', 'I9': '3', 'I8': '2',
                          'I1': '7', 'I3': '8', 'I2': '1', 'I5': '6',
                          'I4': '5', 'I7': '9', 'I6': '4', 'A1': '2',
                          'A3': '7', 'A2': '6', 'E9': '7', 'A4': '9',
                          'A7': '3', 'A6': '5', 'A9': '1', 'A8': '8',
                          'E7': '6', 'E6': '2', 'E1': '3', 'E3': '4',
                          'E2': '8', 'E8': '5', 'A5': '4', 'H8': '6',
                          'H9': '4', 'H2': '3', 'H3': '5', 'H1': '9',
                          'H6': '1', 'H7': '7', 'H4': '2', 'H5': '8',
                          'D8': '9', 'D9': '2', 'D6': '8', 'D7': '1',
                          'D4': '4', 'D5': '3', 'D2': '7', 'D3': '6',
                          'D1': '5'}

    def test_solve(self):
        self.assertEqual(solution.solve(self.diagonal_grid),
                         self.solved_diag_sudoku)


# class TestBasicSudoku(unittest.TestCase):
class TestBasicSudoku(object):
    basic_1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95.'
    basic_1 += '.8..2.3..9..5.1.3..'
    solved_1 = {'A1': '4', 'A2': '8', 'A3': '3', 'A4': '9', 'A5': '2',
                'A6': '1', 'A7': '6', 'A8': '5', 'A9': '7', 'B1': '9',
                'B2': '6', 'B3': '7', 'B4': '3', 'B5': '4', 'B6': '5',
                'B7': '8', 'B8': '2', 'B9': '1', 'C1': '2', 'C2': '5',
                'C3': '1', 'C4': '8', 'C5': '7', 'C6': '6', 'C7': '4',
                'C8': '9', 'C9': '3', 'D1': '5', 'D2': '4', 'D3': '8',
                'D4': '1', 'D5': '3', 'D6': '2', 'D7': '9', 'D8': '7',
                'D9': '6', 'E1': '7', 'E2': '2', 'E3': '9', 'E4': '5',
                'E5': '6', 'E6': '4', 'E7': '1', 'E8': '3', 'E9': '8',
                'F1': '1', 'F2': '3', 'F3': '6', 'F4': '7', 'F5': '9',
                'F6': '8', 'F7': '2', 'F8': '4', 'F9': '5', 'G1': '3',
                'G2': '7', 'G3': '2', 'G4': '6', 'G5': '8', 'G6': '9',
                'G7': '5', 'G8': '1', 'G9': '4', 'H1': '8', 'H2': '1',
                'H3': '4', 'H4': '2', 'H5': '5', 'H6': '3', 'H7': '7',
                'H8': '6', 'H9': '9', 'I1': '6', 'I2': '9', 'I3': '5',
                'I4': '4', 'I5': '1', 'I6': '7', 'I7': '3', 'I8': '8',
                'I9': '2'}
    basic_2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7'
    basic_2 += '.5..2.....1.4......'
    solved_2 = {'A1': '4', 'A2': '1', 'A3': '7', 'A4': '3', 'A5': '6',
                'A6': '9', 'A7': '8', 'A8': '2', 'A9': '5', 'B1': '6',
                'B2': '3', 'B3': '2', 'B4': '1', 'B5': '5', 'B6': '8',
                'B7': '9', 'B8': '4', 'B9': '7', 'C1': '9', 'C2': '5',
                'C3': '8', 'C4': '7', 'C5': '2', 'C6': '4', 'C7': '3',
                'C8': '1', 'C9': '6', 'D1': '8', 'D2': '2', 'D3': '5',
                'D4': '4', 'D5': '3', 'D6': '7', 'D7': '1', 'D8': '6',
                'D9': '9', 'E1': '7', 'E2': '9', 'E3': '1', 'E4': '5',
                'E5': '8', 'E6': '6', 'E7': '4', 'E8': '3', 'E9': '2',
                'F1': '3', 'F2': '4', 'F3': '6', 'F4': '9', 'F5': '1',
                'F6': '2', 'F7': '7', 'F8': '5', 'F9': '8', 'G1': '2',
                'G2': '8', 'G3': '9', 'G4': '6', 'G5': '4', 'G6': '3',
                'G7': '5', 'G8': '7', 'G9': '1', 'H1': '5', 'H2': '7',
                'H3': '3', 'H4': '2', 'H5': '9', 'H6': '1', 'H7': '6',
                'H8': '8', 'H9': '4', 'I1': '1', 'I2': '6', 'I3': '4',
                'I4': '8', 'I5': '7', 'I6': '5', 'I7': '2', 'I8': '9',
                'I9': '3'}

    # def test_basic1(self):
    #     self.assertEqual(solution.solve(self.basic_1), self.solved_1)

    # def test_basic2(self):
    #     self.assertEqual(solution.solve(self.basic_2), self.solved_2)


if __name__ == '__main__':
    unittest.main()
