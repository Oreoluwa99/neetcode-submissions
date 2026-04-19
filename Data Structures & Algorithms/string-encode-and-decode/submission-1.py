class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            # check until you reach #
            while s[j] != "#":
                j += 1
            length_str = int(s[i:j]) # the real number
            # read the number from # to the end of the digit
            word = s[j+1: j+1+length_str]
            result.append(word)
            i = j+1+length_str

        return result