class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        bulbset = sorted(set(bulbs))
        on_off = False
        seen = {item: False for item in bulbset}

        for b in bulbs:
            seen[b] = not seen[b]

        answer = [ key for key, value in seen.items() if value == True]
        return answer

        
        