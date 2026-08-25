class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = 0
        mural = []

        for letra in s:
            if letra != " ":
              out += 1
            else:
              if out > 0:
                mural.append(out)
                out = 0
        if out > 0:
            mural.append(out)
        return mural[-1] if mural else 0