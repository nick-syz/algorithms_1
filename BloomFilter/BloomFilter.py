# https://skillsmart.ru/algo/15-121-cm/z0b3da83s2.html

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = 0

    def hash1(self, string):
        number = 0
        for element in string:
            number = (number*17 + ord(element)) % self.filter_len
        return 1 << number

    def hash2(self, string):
        number = 0
        for element in string:
            number = (number*223 + ord(element)) % self.filter_len
        return 1 << number

    def add(self, added_string):
        if self.filter_len:
            self.bit_array = self.bit_array | self.hash1(added_string) | self.hash2(added_string)

    def is_value(self, string):
        if self.filter_len and self.bit_array:
            mask = self.hash1(string) | self.hash2(string)
            return mask == self.bit_array & mask
        return False
