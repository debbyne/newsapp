import unittest
from app import Source

class SourceTest(unittest.TestCase):
    '''
    Test for the source class
    '''
    def setUp(self):
        '''
        Set up method to run before each test
        '''
        self.new_source = Source('bbc-news','BBC NEWS','general','"https://www.bbc.co.uk')
    def __init__(self):
        self.assertTrue(isinstance(self.new_source,Source))