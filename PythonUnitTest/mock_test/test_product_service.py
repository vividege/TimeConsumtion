import unittest
from unittest.mock import patch, MagicMock

from PythonUnitTest.service.product_service import ProductService


class TestProductService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = ProductService()

    def tearDown(self) -> None:
        self.service = None

    @patch("PythonUnitTest.service.product_service.urlopen")
    @patch("PythonUnitTest.service.product_service.Request.__new__")  # 因为是创建了Request()对象，所以要mock Request.__new__()方法
    def test_download_img_with_exception(self, request_mock, urlopen_mock):
        # Setup
        url = "http://www.ggole.com/a.jpg"
        urlopen_return_mock = MagicMock()  # urlopen_return返回的是一个context manager 对象
        webfile_mock = MagicMock()
        urlopen_mock.return_value = urlopen_return_mock
        urlopen_return_mock.__enter__.return_value = webfile_mock
        webfile_mock.read.return_value = None
        # mock Request()
        # mock urlopen()
        # mock read()

        with self.assertRaises(Exception):
            # Action
            self.service.download_img(url)

            # Assert

    @patch("builtins.open")
    @patch("os.path.basename")
    @patch("PythonUnitTest.service.product_service.urlopen")
    @patch("PythonUnitTest.service.product_service.Request.__new__")  # 因为是创建了Request()对象，所以要mock Request.__new__()方法
    def test_download_img_with_success(self, request_mock, urlopen_mock, basename_mock, open_mock):
        # Setup
        url = "http://www.ggole.com/a.jpg"
        urlopen_return_mock = MagicMock()  # urlopen_return返回的是一个context manager 对象
        webfile_mock = MagicMock()
        urlopen_mock.return_value = urlopen_return_mock
        urlopen_return_mock.__enter__.return_value = webfile_mock
        webfile_mock.read.return_value = "not none"
        basename_mock.return_value = "fff"
        # open_mock = MagicMock()

        result = self.service.download_img(url)

        # Assert
        self.assertEqual("Download image successfully, fff", result)
