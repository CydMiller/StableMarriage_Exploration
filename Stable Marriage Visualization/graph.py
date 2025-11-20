'''
    Filename: Visualization_Graph.py
    Author: Cydney Miller
    Date Created: 11/20/2025
    Date Updated: 11/20/2025
    Purpose: Class to create representative graphs in the terminal.
'''
from Colors import bcolors
class Graph():
    def __init__(self, men, women, proposals, engagements, marriages):
        self.__men = men
        self.__women = women
        self.__proposals = proposals
        self.__engagements = engagements
        self.__marriages = marriages

    def print_row_one(self):
            print(f"------  {bcolors.WOMEN}------  ------  ------  ------")
            print("|    |  | w1 |  | w2 |  | w3 |  | w4 |")
            print("|    |  |    |  |    |  |    |  |    |")
            print("------  ------  ------  ------  ------")

    def print_a1(self, proposed = False, engaged = False):
          if proposed == True:
                print
          
    def print_graph(self):
            print("------  ------")
            print("|    |  |    |")
            print("|    |  |    |")
            print("------  ------")
            print("------")
            print("| m1 |")
            print("|    |")
            print("------")