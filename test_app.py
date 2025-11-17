import os  #for ignoring github actions for gui tests
import unittest
RUNNING_IN_GITHUB = os.environ.get("GITHUB_ACTIONS") == "true"  #stops running gui tests in github actions as they dont work
from main import AppWindow, InputTelephoneNo, InputName



@unittest.skipIf(RUNNING_IN_GITHUB, "Skipping GUI tests on GitHub Actions (no display available)") #skips tests when running in github actions
class TestSmoke(unittest.TestCase):
    def test_create_app(self):
        """Tries to create app window."""
        try:
            app = AppWindow() #creates app
            app.destroy() #destroys app
        except Exception as e:
            self.fail(f"test_create_app failed, error: {e}")

    def test_required_modules(self):
        """Tries to import required modules."""
        try:
            import tkinter as tk
            from tkinter import ttk
            import customtkinter as ctk
            import csv
            import re
            from CTkMessagebox import CTkMessagebox
            import tkinter.messagebox as messagebox
            from datetime import datetime
        except Exception as e:
            self.fail(f"test_required_modules failed, error: {e}")

    def test_csv_exists(self):
        """Tries to open CSV."""
        try:
            with open("table_data.csv", newline="", encoding='utf-8') as f:
                f.readline()
        except FileNotFoundError as e:
            self.fail(f"test_csv_exists failed, error: {e}")
            
@unittest.skipIf(RUNNING_IN_GITHUB, "Skipping GUI tests on GitHub Actions (no display available)") #skips tests when running in github actions
class CheckDataValidation(unittest.TestCase):
    def test_phone_number_validation(self):
        """Checks if phone number validation is working correctly."""

        #creates app instance
        self.app = AppWindow()
        self.telephone_input = InputTelephoneNo(self.app.menu)
        
        def number_validation_pass(list_numbers):
            """Checks valid phone numbers."""
            for number in list_numbers:
                print("Testing valid number", number,":",end=" - ")
                with self.subTest(number=number):
                    isvalid, message = self.telephone_input.validate_telephone_no(number)
                    self.assertTrue(isvalid, f"Failed: valid_numbers_home {number} failed validation. Message: {message}")
                    

        def number_validation_fail(list_numbers):
            """Checks invalid phone numbers."""
            for number in list_numbers:
                print("Testing invalid number", number,":",end=" - ")
                with self.subTest(number=number):
                    isvalid, message = self.telephone_input.validate_telephone_no(number)
                    self.assertFalse(isvalid, f"Failed: valid_numbers_home {number} failed validation. Message: {message}")

        valid_numbers_home = ["0123456789","01234567890","0198765432","01987654321","01619872222","01619872223","01712765432","01712765433","01865748392","01865748393","0201234567","02012345678","02899887766","02899887767","02311223344","02311223345","01415556666","01415556667","01316667777","01316667778"]
        valid_numbers_mobile = ["07123456789","07234567890","07345678901","07456789012","07567890123","07678901234","07789012345","07890123456","07901234567","07912345678","07923456789","07934567890","07945678901","07956789012","07967890123","07978901234","07989012345","07990123456","07012345678","07023456789"]
        valid_numbers_mobile_area_code = ["+447123456789","+447234567890","+447345678901","+447456789012","+447567890123","+447678901234","+447789012345","+447890123456","+447901234567","+447012345678"]

        invalid_numbers_mobile = ["0712345678","071234567890","06123456789","00123456789","07A23456789","07!23456789","07 123456789","+07123456789","++447123456789","447123456789","07456-789012","07_123456789","07.123456789","07/123456789","07(123456789)","07+123456789","07-123456789","079648484823","07964a84823","abcdefghijk"]
        invalid_numbers_home = ["1234567890","03123456789","04123456789","011234567","011234567890","+441234567890","01 23456789","01-23456789","01.23456789","01/23456789","01A3456789","01_3456789","(01)23456789","01+3456789","01--3456789","0101234567899","abcdefghij","0123456789a","02!23456789","02012345678b"]
        
        number_validation_pass(valid_numbers_home)
        number_validation_pass(valid_numbers_mobile)
        number_validation_pass(valid_numbers_mobile_area_code)

        number_validation_fail(invalid_numbers_mobile)
        number_validation_fail(invalid_numbers_home)

        #destroys app instance
        self.app.destroy()


    def test_name_validation(self):
        """Checks if name validation is working correctly."""

        #creates app instance
        self.app = AppWindow()
        self.name_input = InputName(self.app.menu)
        
        def name_validation_pass(name_type: str, list_names: list[str]):
            """Checks valid names."""
            for name in list_names:
                print(f"Testing valid {name_type} name {name}:",end=" - ")
                with self.subTest(name=name):
                    isvalid, message = self.name_input.validate_name(name,name_type)
                    self.assertTrue(isvalid, f"Failed: {name_type} name {name} failed validation. Message: {message}")
                    

        valid_first_names = ["John","Emily","Michael","Sarah","Daniel","Olivia","Thomas","Emma","James","Ava","William","Grace","Samuel","Chloe","Benjamin","Lucy","Ethan","Sophie","Alexander","Isabella"]
        valid_middle_names = ["Marie","James","Anne","Lee","Grace","Rose","John","Paul","Jane","Kate","Claire","Louise","Jean","May","Eve","O'Neil","Jo-Anne","Mary","Skye","Alan"]
        valid_second_names = ["Smith","Johnson","Williams","Brown","Taylor","Anderson","O'Connor","McDonald","O'Brien","Clark","Roberts","Wilson","Thompson","Harrison","Walker","Evans","King","Bennett","Scott","Turner"]

        invalid_first_names = ["John3","@Emily","M!chael","S#rah","Dani3l","0livia","Th0mas","Emm@","Jam#s","Av@","Will!am","Gr@ce","Samue1","Chl0e","Benjam!n","Luc#","Eth@n","Soph!e","Alexand3r","Isabell@"]
        invalid_middle_names = ["Mar1e","Jam3s","Ann3","L33","Gr@ce","R0se","J0hn","P@ul","Jan3","K@te","Cl@ire","L0uise","J3an","M@y","Ev3","O'N3il","J0-Anne","M@ry","Sk!e","Al@n"]
        invalid_second_names = ["Sm!th","Johns0n","Willi@ms","Br0wn","Tayl0r","Anders0n","O'C0nnor","McD0nald","O'Br!en","Cl@rk","R0berts","Wils0n","Th0mpson","H@rrison","W@lker","Ev@ns","K!ng","Benn3tt","Sc0tt","T0rner"]

        name_validation_pass("first", valid_first_names)
        name_validation_pass("middle", valid_middle_names)
        name_validation_pass("second", valid_second_names)



        #destroys app instance
        self.app.destroy()



if __name__ == "__main__":
    unittest.main()