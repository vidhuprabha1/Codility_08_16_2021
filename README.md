Use python3 to run app.py file

git@github.com:vidhuprabha1/Codility_08_16_2021.git

There are N number of apple trees, indexed from 1 to N. While A can be assumed as list of N and each value of A represents number of the apple in the tree. Person1 has to pick apple from K adjasant trees and Person2 has to pick apple from L adjasant trees. find out the maximum number of apple person1 and person 2 can pick. Person1 and Person2 can not pick apple from same tree.

def solution(A, K, L):
 1<= L <=N
 1<= K <=N
 
if total of K and L > N, return -1

