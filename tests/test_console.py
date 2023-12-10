#!/user/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.held_output = StringIO()

    def tearDown(self):
        self.held_output.close()

    def test_quit_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.assertTrue(self.console.onecmd("quit"))
        self.assertEqual(self.held_output.getvalue().strip(), "")

    def test_EOF_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.assertTrue(self.console.onecmd("EOF"))
        self.assertEqual(self.held_output.getvalue().strip(), "")

    def test_create_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        self.assertTrue(self.held_output.getvalue().strip().isalnum())

    def test_show_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
            obj_id = self.held_output.getvalue().strip()
            self.held_output.truncate(0)
            self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn("BaseModel", self.held_output.getvalue())

    def test_destroy_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
            obj_id = self.held_output.getvalue().strip()
            self.held_output.truncate(0)
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.console.onecmd("show BaseModel {}".format(obj_id))
        self.assertIn("** no instance found **", self.held_output.getvalue())

    def test_all_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
            self.held_output.truncate(0)
            self.console.onecmd("all")
        self.assertIn("BaseModel", self.held_output.getvalue())

    def test_count_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
            self.held_output.truncate(0)
            self.console.onecmd("count BaseModel")
        self.assertEqual(self.held_output.getvalue().strip(), "1")

    def test_update_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
            obj_id = self.held_output.getvalue().strip()
            self.held_output.truncate(0)
            self.console.onecmd(f"update BaseModel {obj_id} name 'new_name'")
            self.console.onecmd(f"show BaseModel {obj_id}")
        self.assertIn("new_name", self.held_output.getvalue())


if __name__ == '__main__':
    unittest.main()
