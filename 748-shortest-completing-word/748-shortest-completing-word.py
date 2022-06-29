class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        license_plate = []
        for ch in licensePlate.lower():
            if not ch.isnumeric() and ch !=' ':
                license_plate.append(ch)

        words.sort(key=len)

        for word in words:
            for ch in license_plate:
                if ch not in word or license_plate.count(ch) > word.count(ch):
                    break
            else:
                return word