import unittest

from communication import email


class TestEmail(unittest.TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            email.Email("asdf.asdf")

    def test_str(self):
        jenicto_email = email.Email("jenicto2@fel.cvut.cz")
        self.assertEqual("jen*****@fel.cvut.cz", str(jenicto_email))

    def test_top_level_domain(self):
        jenicto_email = email.Email("jenicto2@fel.cvut.cz")
        self.assertEqual("cz", jenicto_email.top_level_domain)

    def test_eq(self):
        jenicto_email = email.Email("jenicto2@fel.cvut.cz")
        self.assertEqual(jenicto_email, email.Email("jenicto2@fel.cvut.cz"))
        self.assertEqual(jenicto_email, "jenicto2@fel.cvut.cz")

    def test_suggest_different_email(self):
        input_email = email.Email("jenicto@fel.cvut.cz")
        result_email = email.Email("jenicto2@fel.cvut.cz")
        self.assertEqual(result_email, email.Email.suggest_different_email(input_email))


class TestGmail(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(email.Gmail("jenicto"), email.Email("jenicto@gmail.com"))


if __name__ == '__main__':
    unittest.main()
