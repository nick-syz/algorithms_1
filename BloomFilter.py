# https://skillsmart.ru/algo/15-121-cm/z0b3da83s2.html

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.arr = [0] * f_len

    def hash1(self, str1):
        i = 0
        for c in str1:
            i = (i*17 + ord(c)) % self.filter_len
        return i

    def hash2(self, str1):
        j = 0
        for c in str1:
            j = (j*223 + ord(c)) % self.filter_len
        return j

    def add(self, str1):
        self.arr[self.hash1(str1)] = 1
        self.arr[self.hash2(str1)] = 1

    def is_value(self, str1):
        if self.arr[self.hash1(str1)] and self.arr[self.hash2(str1)]:
            return True
        return False
