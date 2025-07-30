"""
Test file for file operations learning exercises.
This demonstrates how to write tests for your Python learning projects.
"""

import unittest
from pathlib import Path
import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the modules we want to test
# Note: We'll import these when we create proper modules

class TestFileOperations(unittest.TestCase):
    """Test cases for file operations learning exercises."""
    
    def test_pathlib_import(self):
        """Test that pathlib can be imported correctly."""
        try:
            from pathlib import Path
            self.assertTrue(True, "pathlib.Path imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import pathlib.Path: {e}")
    
    def test_path_creation(self):
        """Test creating a Path object."""
        from pathlib import Path
        test_path = Path('test', 'file', 'path')
        self.assertIsInstance(test_path, Path)
        self.assertEqual(str(test_path), 'test/file/path')
    
    def test_file_exists(self):
        """Test checking if a file exists."""
        from pathlib import Path
        # Create a temporary file for testing
        test_file = Path('test_file.txt')
        test_file.write_text('test content')
        
        self.assertTrue(test_file.exists())
        
        # Clean up
        test_file.unlink()
    
    def test_file_reading(self):
        """Test reading from a file."""
        from pathlib import Path
        # Create a test file
        test_file = Path('test_read.txt')
        test_content = 'Hello, this is a test file!'
        test_file.write_text(test_content)
        
        # Read the file
        read_content = test_file.read_text()
        self.assertEqual(read_content, test_content)
        
        # Clean up
        test_file.unlink()

if __name__ == '__main__':
    unittest.main() 