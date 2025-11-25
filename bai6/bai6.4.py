print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
class RomanToInt:
    def __init__(self):
        self.values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self, roman):
        total = 0
        prev = 0
        for ch in reversed(roman):
            value = self.values[ch]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value
        return total

converter = RomanToInt()
print(converter.convert("MCMIV"))   
print(converter.convert("XIV"))     
print(converter.convert("XLII"))    
