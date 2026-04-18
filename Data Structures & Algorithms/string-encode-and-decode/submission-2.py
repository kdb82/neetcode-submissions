class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = [f"{len(s)}#{s}" for s in strs]
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        start = 0
        res = []
        while start < len(s):
            end = s.find("#", start)
            length = int(s[start:end])
            word = s[end+1:end+1+length]
            res.append(word)
            start = end + 1 + length

        return res