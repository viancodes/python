from typing import List
from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        L = len(beginWord)
        # parents[w] = set of words that can reach w on a shortest path
        parents = defaultdict(set)

        # BFS
        queue = deque([beginWord])
        found_end = False

        # We'll remove words level-by-level so we don't revisit them in longer paths
        while queue and not found_end:
            level_visited = set()  # words first seen at this BFS level

            for _ in range(len(queue)):
                word = queue.popleft()

                # Generate neighbors by changing one character
                for i in range(L):
                    orig = word[i]
                    for c_ord in range(ord('a'), ord('z') + 1):
                        c = chr(c_ord)
                        if c == orig:
                            continue
                        next_word = word[:i] + c + word[i+1:]

                        if next_word in word_set:
                            if next_word not in level_visited:
                                level_visited.add(next_word)
                                queue.append(next_word)
                            # Record parent even if already discovered this level,
                            # because there can be multiple shortest parents.
                            parents[next_word].add(word)

                            if next_word == endWord:
                                found_end = True

            # Remove this level's words from the pool so they aren't used again
            word_set -= level_visited

        if not found_end:
            return []

        # Backtrack from endWord to beginWord using parents to enumerate all shortest paths
        results: List[List[str]] = []
        path: List[str] = [endWord]

        def dfs(word: str) -> None:
            if word == beginWord:
                results.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return results

