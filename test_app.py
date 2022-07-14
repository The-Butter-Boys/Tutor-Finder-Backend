import unittest
import app

class TestApp(unittest.TestCase):
  def test_users(self):
    result = app.users()
    assertIsNotNone(result)
  def test_courses(self):
    result = app.courses()
    assertIsNotNone(result)
  def test_to_dict(self):
    result = app.Course.to_dict()
    assertIsNotNone(result)
    
if __name__ == '__main__':
  unittest.main()
