My implementation performs a BFS lookup of a user in each group and subgroup of that group, which takes O(n^m) time of n users per group and m max depth of subgroups.
The algorithm takes care of preventing users from assigning immediate parent groups to immediate subgroups of their children, which would result in an infinite loop when calling the BFS search function.
This safeguard takes along with a safeguard to prevent duplicate groups in subgroups makes the insertion time of a new subgroup O(n) with n=number of subgroups rather than O(1) as presented in the starter code.
However it's still possible to insert a parent group to a subgroup of that parent if the relationship is two or more levels away. 
Allowing the search algorithm to work for a multi-level loop in a graph of groups would require creating a unique set of groups and subgroups within a given group, keeping track of groups already visited, and then traversing through all unique groups and subgroups only once skipping those already visited, and attempting to find the given user in any of the group or subgroups. This would require the same worse case O(n^m) time and space complexity as my BFS implementation and has a more expensive average case time and space complexity.