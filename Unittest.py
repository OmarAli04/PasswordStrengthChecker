import unittest

from Functions import feedback


class Test(unittest.TestCase):

    def test_weak(self):
        username = 'user'
        password = 'password'
        self.assertEqual(feedback(username, password), '🟥 Your password is weak')

    def test_medium(self):
        username = 'User'
        password = 'UserPassword@2'
        self.assertEqual(feedback(username, password), '🟨 Your password is medium strength')

    def test_strong(self):
        username = 'USER'
        password = 'Awwr@29934'
        self.assertEqual(feedback(username, password), '🟩 Your Password is strong')


if __name__ == '__main__':
    unittest.main()