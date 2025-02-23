from collections import deque
import string
from node import Node
from dictionary import Dictionary

class Search:
    """
        Implements search algorithms for word transformations.
    """
    def __init__(self, start_word="", end_word=""):
        """
        Initializes the Search object with start and end words.

        Args:
            start_word (str): The word to start the transformation from.
            end_word (str): The target word to transform into.
        """    
        self.start_word = start_word
        self.end_word = end_word
        self.dictionary = Dictionary("words.txt")

    def bfs(self):
            """
            Performs Breadth-First Search (BFS).
        
            Returns:
                Node or None: The final Node representing the end_word if a path is found, otherwise None.
            """
            # Check if words have same length            
            # Initialize data structures
            queue = deque()
            visited = set()
            
            # Create and add start node
            start_node = Node(self.start_word)
            queue.append(start_node)
            visited.add(self.start_word)
            visited_with_duplicate_count = 0
            
            # BFS algorithm
            while queue:
                current_node = queue.popleft()
                current_word = current_node.value
                
                visited_with_duplicate_count += 1
                # Check if we've reached the target word
                if current_word == self.end_word:
                    print("Number of nodes expanded: ",visited_with_duplicate_count, "Number of nodes visited: ", len(visited), "Solution Length", current_node.get_depth())
                    return current_node
                    
                # Try changing one letter at a time
                for i in range(len(current_word)):
                    word_chars = list(current_word)
                    for c in string.ascii_lowercase:
                        word_chars[i] = c
                        next_word = ''.join(word_chars)
                        
                        # Check if word exists and hasn't been visited
                        if (next_word not in visited and 
                            self.dictionary.search_word(next_word)):
                            next_node = Node(next_word)
                            next_node.set_parent(current_node)
                            queue.append(next_node)
                            visited.add(next_word)             
            return None
    
    def dfs(self):
        """
        Performs Depth-First Search (DFS).

        Returns:
            Node or None: The final Node representing the end_word if a path is found, otherwise None.
        """
        # TODO: Implement DFS logic
        stack = []
        visited = set()
        visited_with_duplicate_count = 0
    
    # Create and add start node
        start_node = Node(self.start_word)
        stack.append(start_node)
    
        while stack:
            current_node = stack.pop() 
            current_word = current_node.value

            visited_with_duplicate_count += 1
            if current_word not in visited:
                visited.add(current_word)
            
            # Check if we've reached the target word
            if current_word == self.end_word:
                print("Number of nodes expanded: ",visited_with_duplicate_count, "Number of nodes visited: ", len(visited), "Solution Length", current_node.get_depth())
                return current_node
            
            # Try changing one letter at a time
            for i in range(len(current_word)):
                word_chars = list(current_word)
                for c in string.ascii_lowercase:
                    word_chars[i] = c
                    next_word = ''.join(word_chars)
                    
                    # Check if word exists and hasn't been visited
                    if (next_word not in visited and 
                        self.dictionary.search_word(next_word)):
                        next_node = Node(next_word)
                        next_node.set_parent(current_node)
                        stack.append(next_node)
        return None

    def print_transformations(self, word_list):
        """
        Helper method to print the sequence of words
        Args:
            world_list(list) Sequence of words 
        """
        print(" --> ".join(word_list))
