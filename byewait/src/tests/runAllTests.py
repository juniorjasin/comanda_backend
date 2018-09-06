import unittest
from testLogin import TestLogin
from testMenu import TestMenu
from testPedido import TestPedido
from testRegister import TestRegister
from testRestaurantes import TestRestaurante
from testMenuItemScore import TestMenuItemScore
from testCredenciales import TestCredenciales

if __name__ == '__main__':
    test_classes_to_run = [TestLogin, TestMenu, TestPedido, TestRegister, TestRestaurante, TestMenuItemScore, TestCredenciales]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)