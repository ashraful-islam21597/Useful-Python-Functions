# useful python functions for string manipulation


from itertools import permutations


class StringMethods(object):

    def Longest_unique_substring_length(self, input_string):

        # the length of longest substring without reapeating characters
        # input parm string
        # return length

        helper_string = ""
        lengths = []
        for i in input_string:
            if i not in helper_string:
                helper_string = helper_string + i
            else:
                lengths.append(len(helper_string))
                s1 = helper_string[helper_string.index(i) + 1:] + i
        lengths.append(len(helper_string))
        return (max(lengths))

    def unique_substrings(self, input_string):

        # the list of all substring without reapeating characters
        # input parm string
        # return list of all substring without reapeating characters

        characters = set(input_string)
        list_of_strings = []
        for i in range(1, len(characters) + 1):
            for j in list(permutations(characters, i)):
                s1 = "".join(j)
                if s1 in input_string:
                    list_of_strings.append(s1)

        return list_of_strings

    def Longest_Palindromic_Substring(self, s):

        # Longest Palindromic Substring
        # input parm string
        # return alindromic Substring

        index = 0
        long_palindrome = ""
        if s == s[::-1]:
            return s
        elif len(set(s)) == len(s):
            return s[0]
        else:
            for i in s:
                reverse_string = list(s[::-1])
                if s.count(i) > 1:
                    for j in range(s.count(i) - 1):
                        z = reverse_string.index(i)
                        sub_string = s[index:(len(reverse_string) + 1 - (z + 1))]
                        reverse_string.pop(z)
                        if sub_string == sub_string[::-1]:
                            if len(long_palindrome) < len(sub_string):
                                long_palindrome = sub_string
                index += 1
            return long_palindrome

    def Longest_palindromic_substring_list(self, input_string):

        # the list of all palindromic substring
        # input parm string
        # return list of all palindromic substring without reapeating characters

        list_of_strings = []
        for i in range(1, len(input_string) + 1):
            for j in list(permutations(list(input_string), i)):
                s1 = "".join(j)
                if s1 in input_string and s1 == s1[::-1]:
                    list_of_strings.append(s1)

        return set(list_of_strings)
