# Railfence Implemenation using python

class Solution:
    def convert(self, s, n):
        if n == 1:
            return s
        
        result = []
        length = len(s)
        k = 2 * (n - 1)
        
        for i in range(n):
            j = i
            while j < length:
                result.append(s[j])
                if i != 0 and i != n - 1:
                    k1 = k - (2 * i)
                    k2 = j + k1
                    if k2 < length:
                        result.append(s[k2])
                j += k
        return ''.join(result)

    def reverse_convert(self, s, n):
        if n == 1:
            return s
        
        original_string = [''] * len(s)
        length = len(s)
        k = 2 * (n - 1)
        idx = 0
        
        for i in range(n):
            j = i
            while j < length:
                original_string[j] = s[idx]
                idx += 1
                if i != 0 and i != n - 1:
                    k1 = k - (2 * i)
                    k2 = j + k1
                    if k2 < length:
                        original_string[k2] = s[idx]
                        idx += 1
                j += k
                
        return ''.join(original_string)


# Taking input from the user
input_str = input("Enter the input string: ")
input_n = int(input("Enter the value of n: "))

solution = Solution()
converted_string = solution.convert(input_str, input_n)
print("Converted string:", converted_string)

reverse_input_n = int(input("Enter the value of n for reverse conversion: "))
reverse_plain_text = solution.reverse_convert(converted_string, reverse_input_n)
print("Reverse converted plain text:", reverse_plain_text)