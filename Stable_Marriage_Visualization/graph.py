'''
    Filename: graph.py
    Author: Cydney Miller
    Date Created: 11/20/2025
    Date Updated: 11/20/2025
    Purpose: Class to create representative graphs in the terminal.
'''
from Stable_Marriage_Visualization.colors import bcolors

class Graph():
    # TODO: rethink the structure of my graph and in turn change the contructor
    def __init__(self, men, women, proposals, engagements, marriages):
        self.__men = men
        self.__women = women
        self.__proposals = proposals
        self.__engagements = engagements
        self.__marriages = marriages

    def print_row_one(self):
            print(f"------  {bcolors.WOMEN}------  ------  ------  ------{bcolors.RESET}")
            print(f"|    |  {bcolors.WOMEN}| w1 |  | w2 |  | w3 |  | w4 |{bcolors.RESET}")
            print(f"|    |  {bcolors.WOMEN}|    |  |    |  |    |  |    |{bcolors.RESET}")
            print(f"------  {bcolors.WOMEN}------  ------  ------  ------{bcolors.RESET}")

    def print_a1(self, proposed = False, engaged = False):
        if proposed == True:
            print(f"{bcolors.PROPOSED}------{bcolors.RESET}")
            print(f"{bcolors.PROPOSED}|////|{bcolors.RESET}")
            print(f"{bcolors.PROPOSED}|////|{bcolors.RESET}")
            print(f"{bcolors.PROPOSED}------{bcolors.RESET}")
        elif engaged == True:
            print(f"{bcolors.ENGAGED}------{bcolors.RESET}")
            print(f"{bcolors.ENGAGED}|////|{bcolors.RESET}")
            print(f"{bcolors.ENGAGED}|////|{bcolors.RESET}")
            print(f"{bcolors.ENGAGED}------{bcolors.RESET}")
        else:
            print("------")
            print("|    |")
            print("|    |")
            print("------")
            
          
    def print_graph(self):
            print("------  ------")
            print("|    |  |    |")
            print("|    |  |    |")
            print("------  ------")
            print("------")
            print("| m1 |")
            print("|    |")
            print("------")