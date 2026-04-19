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

            # Find the # that ends the number 
            while s[j] != "#":
                j += 1
            length_num = int(s[i:j])  # word length

            # get all the numbers before the next digit
            word = s[j+1: j+1+length_num]
            result.append(word)

            # move the pointer to the next
            i = j+1+length_num
        return result