import unittest

from . import app


class TestConfg(unittest.TestCase):
    

    def setUp(self):
        self.request = RequestFactory()
        self.request.session = {}
        self.request.anonymous_user = AnonymousUser()



    @classmethod
    def setUpTestData(cls):
        cls.test_shopping_list = Shopping_list(
            list_name='Sample List',
            list_category = 'Sample Category',
            list_items = [],
            slug='slug'
        )

        cls.test_shopping_list.save()

        # test case for successful registration
    def test_successful_registration(self):
        registration_form = Registration_form(
            user_email='name@example.com',
            user_password='sample',
            message ='sample'
            )
        self.assertTrue(registration_form.validate())


        # test case for user password validation
    def test_user_password_follow_convention(self):
        registration_form = Registration_form(
            user_email='name@example.com',
            user_password='sample',
            message ='sample'
            )
        self.assertFalse(registration_form.validate())



        # test case for account already in existence
    def test_user_account_exists(self):
        registration_form = Registration_form(
           user_email='name@example.com',
            user_password='sample',
            message ='sample'
            )
        self.assertFalse(form.validate())

        # Create a fake user for testing purposes
        @staticmethod
    def _fake_user():
        fake_user = Fake_object(
            usr_name='Felix',
            usr_email='felix@example.com',
        )
        fake_user.password(fake_password='passord')
        fake_user.save()

        return fake_user


        # Test if shopping list have string representation
    def test_shopping_list_as_string(self):
        shopping_list = self._fake_user()
        self.assertEqual(str(shopping_list), 'Shopping List name: {id}'.format(id=shopping_list.pk))


