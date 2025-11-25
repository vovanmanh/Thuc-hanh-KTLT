print("Sinh Vien:Vo Van Manh")
print("MSV:245752021610011")
print("###################")
###################
class ReverseWords:
    def reverse(self, text):
        words = text.split()
        words.reverse()
        return " ".join(words)

r = ReverseWords()
print(r.reverse("ADC .py"))
