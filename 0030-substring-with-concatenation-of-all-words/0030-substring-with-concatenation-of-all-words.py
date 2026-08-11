from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        target = Counter(words)
        result = []

        # Try each possible alignment
        for offset in range(word_len):
            left = offset
            count = 0
            seen = Counter()

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                # Word is not in words
                if word not in target:
                    seen.clear()
                    count = 0
                    left = right + word_len
                    continue

                seen[word] += 1
                count += 1

                # Too many occurrences of this word
                while seen[word] > target[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1

                # Found all required words
                if count == word_count:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1

        return result