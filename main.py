from dictionary import Dictionary
from search import Search

def main():
    print("**************Dictionary usage example**************")
    file_name = "words.txt"
    dict_obj = Dictionary(file_name)
    
    if dict_obj.search_word("test"):
        print("The tested word is in our dictionary")

    print("**************Example to test search implementation **************")
    # start_word = "drivers"
    # end_word = "nearest"
    start_word = input("Press Enter to start the search: ")

    end_word = input("Press Enter to end the search:")
    new_search = Search(start_word, end_word)

    goal_node = new_search.bfs()

    print("**************BFS**************")
    if goal_node is not None:
        while goal_node.get_parent() is not None:
            print(f"{goal_node.value} <-", end="")
            goal_node = goal_node.get_parent()
        print(goal_node.value)
    else:
        print("You are yet to implement the code, try after implementation")

    print("**************DFS**************")
    goal_dfs_node = new_search.dfs()
    if goal_dfs_node is not None:
        while goal_dfs_node.get_parent() is not None:
            print(f"{goal_dfs_node.value} <-", end="")
            goal_dfs_node = goal_dfs_node.get_parent()
        print(goal_dfs_node.value)
    else:
        print("You are yet to implement the code, try after implementation")

if __name__ == "__main__":
    main()
