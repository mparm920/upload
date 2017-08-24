from upload import app
import unittest

class UploadTest(unittest.TestCase):

    def setup(self):
        app.config["SECRET_KEY"] = 'eflex upload page'

    def test_Cant_access_root_endpoint(self):
        self.tester = app.test_client(self)
        res = self.tester.get('/', follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"<label>Login</label>", res.data)

    def test_login_endpoint(self):
        self.tester = app.test_client(self)
        res = self.tester.get('/login', follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"<label>Login</label>", res.data)

    def test_login_redirect(self):
        self.tester = app.test_client(self)
        res = self.tester.post('/login', data=dict(username='mparm920@gmail.com', password='mark'), follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'id="uploadForm"', res.data)

    def test_logout_endpoint(self):
        self.tester = app.test_client(self)
        res = self.tester.get('/logout', follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"<label>Login</label>", res.data)

if __name__ == '__main__':
    unittest.main()