# Word Ladder Search Implementation

## Overview
This project implements a word ladder search problem using both Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms. A word ladder is a puzzle where you need to transform one word into another by changing one letter at a time, with each intermediate step being a valid word.

## Features
- Implementation of BFS and DFS search algorithms
- Dictionary validation of words
- Path finding between two words of equal length
- Performance metrics tracking (nodes expanded, nodes visited, solution length)

## Example
Finding path from "GLASS" to "CLINK":



## Project Structure
- `main.py`: Main program entry point with example usage
- `search.py`: Contains BFS and DFS implementations
- `dictionary.py`: Dictionary class for word validation
- `words.txt`: Dictionary file containing valid words

## Usage
```python
from search import Search

# Create a search instance
search = Search("GLASS", "CLINK")

# Find path using BFS
bfs_result = search.bfs()

# Find path using DFS 
dfs_result = search.dfs()


GitHub Copilot
GLASS → GLANS → CLANS → CLANK → CLINK


## Project Structure
- `main.py`: Main program entry point with example usage
- `search.py`: Contains BFS and DFS implementations
- `dictionary.py`: Dictionary class for word validation
- `words.txt`: Dictionary file containing valid words

## Usage
```python
from search import Search

# Create a search instance
search = Search("GLASS", "CLINK")

# Find path using BFS
bfs_result = search.bfs()

# Find path using DFS 
dfs_result = search.dfs()
Performance Metrics
The implementation tracks:

Number of nodes expanded
Number of nodes visited
Solution path length
Requirements
Python 3.x
No external dependencies required
Course Information
This project is part of an AI course focusing on search algorithms and their implementations in practical applications. ```