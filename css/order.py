from collections import deque


# Recursive function to find preorder traversal of a binary tree
# from its inorder and postorder sequence.
def printPreorder(start, end, postorder, pIndex, dict, stack):

    # base case
    if start > end:
        return pIndex

    # The next element in the postorder sequence from the end will be the root node
    # of subtree formed by sequence `inorder[start, end]`
    value = postorder[pIndex]
    pIndex = pIndex - 1

    # get the current node index in inorder sequence to determine
    # its left and right subtree boundary
    index = dict[value]

    # recur for the right subtree
    pIndex = printPreorder(index + 1, end, postorder, pIndex, dict, stack)

    # recur for the left subtree
    pIndex = printPreorder(start, index - 1, postorder, pIndex, dict, stack)

    # push the value of the current node into the stack
    stack.append(value)

    return pIndex


# Find preorder traversal of a binary tree from its inorder and
# postorder sequence. This function assumes that the input is valid.
# i.e., given inorder and postorder sequence forms a binary tree.
def findPreorder(inorder, postorder):

    # dict is used to efficiently find the index of any element in
    # a given inorder sequence
    dict = {}

    # fill the dictionary
    for i, e in enumerate(inorder):
        dict[e] = i

    # `lastIndex` stores the index of the next unprocessed node from the end
    # of the postorder sequence
    lastIndex = len(inorder) - 1

    # construct a stack to store the preorder sequence
    stack = deque()

    # fill the stack
    printPreorder(0, lastIndex, postorder, lastIndex, dict, stack)

    # print the stack
    print("The preorder traversal is ", end='')
    while stack:
        print(stack.pop(), end=' ')


if __name__ == '__main__':

    ''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /       / \
         /       /   \
        4       5     6
               / \
              /   \
             7     8
    '''

    inorder = ['j', 'e', 'n', 'k', 'o', 'p', 'b',
               'f', 'a', 'c', 'l', 'g', 'm', 'd', 'h', 'i']
    postorder = ['j', 'n', 'o', 'p', 'k', 'e', 'f',
                 'b', 'c', 'l', 'm', 'g', 'h', 'i', 'd', 'a']

    findPreorder(inorder, postorder)
