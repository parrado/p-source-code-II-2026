from unittest import  TestCase
from unittest import main

# This is the class we want to test. So, we need to import it
from pyqt.virtuallab_client import *


class Test(TestCase):
   

    # test case function to check the Person.set_name function
    def test_register(self):
        print("Start register test\n")
        url="http://127.0.0.1:80"
        # Registra un usuario profesor
        name="Alexander"
        id_professor=787878 
        role="professor"
        password_professor="professor_pass"
        self.assertEqual(registerUser(url,name,id_professor,role,password_professor), 'User already registered')
        print("\nFinish register test\n")

    def test_login(self):
            print("Start login test\n")
            url="http://127.0.0.1:80"            
            id_professor=787878            
            password_professor="professor_pass"
            self.assertEqual(openSession(url,id_professor,password_professor), f'openSession called by user {id_professor}')
            print("\nFinish login test\n")



# begin the unittest.main()
main()
