Problem

Link: https://leetcode.com/problems/find-the-duplicate-number/

Pattern:

Floyd’s Tortoise and Hare (Cycle Detection) on an implicit linked list

Key idea (2 lines):

Treat nums like a linked list where i -> nums[i]; the duplicate creates a cycle.
Use slow/fast to meet inside the cycle, then reset one pointer to start to find the cycle entrance = duplicate.

Complexity

Time: O(n)
Space: O(1)