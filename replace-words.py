class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            word = sentence[i]
            for root_word in dictionary:
                if word.startswith(root_word) and len(root_word)<len(word):
                    word = root_word
            sentence[i] = word

        return " ".join(sentence)
