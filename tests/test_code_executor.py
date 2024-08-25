import unittest
from code_executor import CodeExecutor

class TestCodeExecutor(unittest.TestCase):
    def setUp(self):
        self.executor = CodeExecutor()

    def test_execution_success(self):
        code = "declare int x = 10; mov eax, x; print eax;"
        result = self.executor.execute_code(code)
        self.assertEqual(result["status"], "success")
        self.assertIn("Code executed successfully", result["output"])

    def test_code_suggestion(self):
        code = "declare int y = 5; mov ebx, y;"
        result = self.executor.execute_code(code)
        self.assertIn("suggestions", result)

if __name__ == '__main__':
    unittest.main()
