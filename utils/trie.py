class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_title = False
        self.full_title = None  # Stores the full title if this node marks the end of a title

class TitleTrie:
    def __init__(self):
        self.prefix_trie = TrieNode()
        self.suffix_trie = TrieNode()
        self.sorted_titles = {}  # Dictionary to store normalized (sorted) titles for anagram checking

    def get_all_titles(self):
        """
        Retrieve all titles stored in the prefix trie.
        """
        titles = []

        def collect_titles(node, current_title):
            # If the current node marks the end of a title, add the full title to the list
            if node.is_end_of_title:
                titles.append(node.full_title)

            # Recursively collect titles from the children
            for word, child in node.children.items():
                collect_titles(child, current_title + [word])

        # Start collecting from the root of the prefix trie
        collect_titles(self.prefix_trie, [])
        return titles

    def insert_title(self, title):
        """Inserts a title into both the prefix and suffix tries and stores its sorted form."""
        self._insert(self.prefix_trie, title.split(), title, forward=True)
        self._insert(self.suffix_trie, title.split()[::-1], title, forward=False)
        # Add the sorted version of the title for anagram checking
        sorted_title = " ".join(sorted(title.split()))
        self.sorted_titles[sorted_title] = title

    def _insert(self, trie, words, full_title, forward=True):
        """Helper function to insert words into a Trie (either prefix or suffix)."""
        node = trie
        for word in words:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]
        node.is_end_of_title = True
        node.full_title = full_title  # Store the complete title at the end node

    def search_prefix(self, title):
        """Returns all titles that share any prefix with the given title."""
        words = title.split()
        matching_titles = []
        # Attempt to match any prefix of the title
        for i in range(len(words)):
            node = self._find_node(self.prefix_trie, words[:i+1])
            if node:
                matching_titles.extend(self._collect_titles(node))
        return list(set(matching_titles))  # Remove duplicates if any

    def search_suffix(self, title):
        """Returns all titles that share any suffix with the given title."""
        words = title.split()
        matching_titles = []
        # Attempt to match any suffix of the title
        for i in range(len(words)):
            suffix_words = words[i:]  # Get the suffix starting from i-th word
            node = self._find_node(self.suffix_trie, suffix_words[::-1])  # Reverse for suffix Trie
            if node:
                matching_titles.extend(self._collect_titles(node))
        return list(set(matching_titles))  # Remove duplicates if any

    def _find_node(self, trie, words):
        """Helper function to find the node matching a prefix or suffix sequence."""
        node = trie
        for word in words:
            if word in node.children:
                node = node.children[word]
            else:
                return None
        return node

    def _collect_titles(self, node):
        """Collects all titles in the subtree rooted at the given node."""
        matching_titles = []
        if node is None:
            return matching_titles
        if node.is_end_of_title:
            matching_titles.append(node.full_title)
        for child in node.children.values():
            matching_titles.extend(self._collect_titles(child))
        return matching_titles

    def find_combination_titles(self, title, memo=None):
        """
        Checks if a title can be formed by combining existing titles in the trie
        and returns the list of titles used in the combination if possible.
        """
        if memo is None:
            memo = {}
        if title in memo:
            return memo[title]

        words = title.split()
        # Attempt to split the title into prefix and suffix parts
        for i in range(1, len(words)):
            prefix = " ".join(words[:i])
            suffix = " ".join(words[i:])

            # Check if prefix and suffix exist in the trie or can be formed by further splitting
            if self._title_exists(self.prefix_trie, prefix.split()):
                if self._title_exists(self.prefix_trie, suffix.split()):
                    memo[title] = [prefix, suffix]
                    return memo[title]
                else:
                    # Recursively check if suffix can be split into known titles
                    suffix_combination = self.find_combination_titles(suffix, memo)
                    if suffix_combination:
                        memo[title] = [prefix] + suffix_combination
                        return memo[title]

        memo[title] = None
        return None

    def _title_exists(self, trie, words):
        """Checks if a sequence of words exists as a title in the given trie."""
        node = trie
        for word in words:
            if word in node.children:
                node = node.children[word]
            else:
                return False
        return node.is_end_of_title

    def is_anagram_of_existing_title(self, title):
        """
        Checks if the given title is an anagram of any existing title in the Trie
        and returns the matching title if it exists.

        Args:
            title (str): The title to check for anagrams.

        Returns:
            str: The matching title if an anagram exists, None otherwise.
        """
        # Normalize the title by sorting its words
        sorted_title = " ".join(sorted(title.split()))
        # Check if this sorted version exists in the dictionary of sorted titles
        return self.sorted_titles.get(sorted_title, None)

    def print_trie(self, trie, path=None):
        """
        Recursively print all titles in the given trie.
        """
        if path is None:
            path = []

        if trie.is_end_of_title:
            print(" -> ".join(path), "->", trie.full_title)

        for word, child in trie.children.items():
            self.print_trie(child, path + [word])

    def debug_tries(self):
        """
        Prints all titles in the prefix and suffix tries for debugging.
        """
        print("=== Prefix Trie ===")
        self.print_trie(self.prefix_trie)
        print("=== Suffix Trie ===")
        self.print_trie(self.suffix_trie)

