class Group(object):
    # O(1)
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    # O(1)
    def get_groups(self):
        return self.groups

    # O(n) for n group in self.groups to prevent user from adding infinite recursion loops and naming collisions in self.groups
    # O(1) for empty or small sets of self.groups, which is is true in the test cases
    def add_group(self, group):
        if self not in group.groups and group.name not in [group.name for group in self.groups]:
            self.groups.append(group)
        elif self in group.groups:
            raise ValueError("You are attempting to add a parent of a group as a child of a group, which is invalid and would result in an infinite loop when searched")
        elif group.name in [group.name for group in self.groups]:
            raise ValueError("You are attempting to add another group of the same name as a subgroup to a group which already has a child group of that name")

    # O(1) appending to a list
    def add_user(self, user):
        self.users.append(user)

    # O(1) returning a list of self.users
    def get_users(self):
        return self.users

    # O(1) returning self.name
    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if type(user) != str or type(group) != type(Group("some group")):
        raise TypeError("In is_user_in_group(user, group), user must be a string and group must be of type(Group())")
    elif len(user) <= 0:
        raise ValueError("User to search for is invalid because it's a string of length zero")
    elif user == group.get_name() or user in group.get_users():
        return(True)
    else:
        return(bool([is_user_in_group(user, subgroup) for subgroup in group.get_groups()]))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Testing whether the starter code works properly
print(f"Test Case 1: Using starter code, is_user_in_group('sub_child_user' should return True and does return {is_user_in_group('sub_child_user', parent)}\n")

# Test Case 2: Testing invalid arguments for is_user_in_group()
try:
    is_user_in_group(None)
except TypeError:
    print("Test Case 2: 'is_user_in_group(None)' results in a TypeError because it's missing one of two positional argument. Even with an additional argument a TypeError would still "\
        "occur because None is an invalid type of function parameters.\n")

# Test Case 3: Testing infinite recursion possibility by attempting to add a parent to a child group as a child group to the child
try:
    child.add_group(parent)
    is_user_in_group('sub_child_user', parent)
except ValueError:
    print("Test Case 3: running 'child.add_group(parent)' results in a ValueError because it's attempting to add a parent group as a subgroup to a child group in the parent group, which would result in an "\
        "infinite recursion loop when running is_user_in_group()\n")

# Test Case 4: Adding duplicate group names as subgroups to a group:
try:
    another_group = Group("another_group")
    parent.add_group(Group("another_group"))
    parent.add_group(another_group)
except ValueError:
    print("Test Case 4: Adding multiple groups of the same name as a subgroup to a group results in a ValueError\n")

# Test Case 5
parent.add_user("Tim")
child.add_user("Scott")
another_group.add_user("Nick")
print(f"Test Case 5: Testing whether the Group class works correctly with a slightly more complex instance of a Group() results in the return boolean: {is_user_in_group('Nick', parent) and is_user_in_group('Scott', parent)}\n")