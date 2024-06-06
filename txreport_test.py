import unittest

from txreport import *

class TestTxReport(unittest.TestCase):

    def test_get_prev_month(self):
        date_start = datetime.datetime(year=2024, month=5, day=1).date()
        date_end = datetime.datetime(year=2024, month=5, day=31).date()

        new_date_start, new_date_end = get_prev_month(date_start, date_end)
        self.assertEqual(new_date_start.year, 2024)
        self.assertEqual(new_date_start.month, 4)
        self.assertEqual(new_date_start.day, 1)

        self.assertEqual(new_date_end.year, 2024)
        self.assertEqual(new_date_end.month, 4)
        self.assertEqual(new_date_end.day, 30)

    def test_get_network_paratime(self):
        url = 'https://somedomain.com/oasis_stats/mainnet_sapphire_%Y-%m.csv'
        network, paratime = get_network_paratime(url)
        self.assertEqual(network, 'Mainnet')
        self.assertEqual(paratime, 'Sapphire')


    def test_format_url(self):
        url = 'https://somedomain.com/oasis_stats/mainnet_sapphire_%Y-%m.csv'
        d = datetime.datetime(year=2024, month=5, day=1).date()
        new_url = format_url(url, d)
        self.assertEqual(new_url, 'https://somedomain.com/oasis_stats/mainnet_sapphire_2024-05.csv')

if __name__ == '__main__':
    unittest.main()