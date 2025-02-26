import unittest
from src.assignment import (
    test_score, exam_score, all_assignments_completed,
    final_score, passed, letter_grade, honor_roll, can_take_advanced
)

class TestGradeCalculator(unittest.TestCase):
    
    def test_task1_final_score(self):
        """Test if the final score is calculated correctly"""
        expected = (test_score + exam_score) / 2
        self.assertEqual(final_score, expected, 
                         f"Expected final_score to be {expected}, but got {final_score}")

    def test_task2_passed(self):
        """Test if the pass status is determined correctly"""
        expected = final_score >= 60
        self.assertEqual(passed, expected, 
                         f"Expected passed to be {expected}, but got {passed}")

    def test_task3_letter_grade(self):
        """Test if the letter grade is assigned correctly"""
        if final_score >= 90:
            expected = "A"
        elif final_score >= 80:
            expected = "B"
        elif final_score >= 70:
            expected = "C"
        elif final_score >= 60:
            expected = "D"
        else:
            expected = "F"
        
        self.assertEqual(letter_grade, expected, 
                         f"Expected letter_grade to be '{expected}', but got '{letter_grade}'")

    def test_task4_honor_roll(self):
        """Test if the honor roll status is determined correctly"""
        expected = final_score >= 90 and all_assignments_completed
        self.assertEqual(honor_roll, expected, 
                         f"Expected honor_roll to be {expected}, but got {honor_roll}")

    def test_task5_advanced_course(self):
        """Test if the advanced course eligibility is determined correctly"""
        expected = (final_score >= 60 and 
                   (letter_grade == "A" or 
                    (letter_grade == "B" and all_assignments_completed)))
        
        self.assertEqual(can_take_advanced, expected, 
                         f"Expected can_take_advanced to be {expected}, but got {can_take_advanced}")

if __name__ == "__main__":
    unittest.main()