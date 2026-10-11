class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        m = {}
        for w in words:
            m[w] = m.get(w, 0) + 1
        
        sorted_words = sorted(m.items(), key=lambda x: (-x[1], x[0]))
        return [w for w, c in sorted_words[:k]]



        return sorted(m, key=lambda x: x[1], reverse=True)
            

        