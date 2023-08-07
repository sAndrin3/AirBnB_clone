from unittest.mock import patch
import __init__  # Import the __init__ module you provided

def test_file_storage_initialized():
    with patch('models.engine.file_storage.FileStorage.reload') as mock_reload:
        __init__.storage
        mock_reload.assert_called_once()

if __name__ == "__main__":
    test_file_storage_initialized()
    print("All tests passed!")
