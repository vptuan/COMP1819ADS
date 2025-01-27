class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []  # Nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def pop(self):
        """Remove and return the element from the top of the stack."""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()

    def top(self):
        """Return (but do not remove) the element at the top of the stack."""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]


def is_expression_correct(expression):
    """
    Check if the arithmetic expression has balanced grouping symbols.

    Parameters:
        expression (str): The arithmetic expression to check.

    Returns:
        str: "Correct" if the expression is balanced, otherwise "Incorrect".
    """
    stack = ArrayStack()
    opening_symbols = "({["
    closing_symbols = ")}]"
    matching_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening_symbols:
            stack.push(char)  # Push opening symbols onto the stack
        elif char in closing_symbols:
            if stack.is_empty() or stack.top() != matching_pairs[char]:
                return "Incorrect"  # Mismatch or extra closing symbol
            stack.pop()  # Pop the matching opening symbol

    # If the stack is empty, all symbols are balanced
    return "Correct" if stack.is_empty() else "Incorrect"


# Test cases
test_cases = [
    "()(()){([()])}",  # Correct
    "({[])}",          # Incorrect
    "((()(()){([()])}))",  # Correct
    ")(()){([()])}",   # Incorrect
    "(",               # Incorrect
]

for expression in test_cases:
    result = is_expression_correct(expression)
    print(f"Input: {expression}\nOutput: {result}\n")