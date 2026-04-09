#!/usr/bin/env python3
"""
Script to reverse strings.
"""

def reverse_string(text):
    """
    Reverse a given string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    return text[::-1]


def main():
    """Main function to demonstrate string reversal."""
    # Example 1: Reverse a simple string
    example1 = "abc"
    print(f"Original: {example1}")
    print(f"Reversed: {reverse_string(example1)}")
    print()
    
    # Example 2: Reverse a longer string
    example2 = "Hello, World!"
    print(f"Original: {example2}")
    print(f"Reversed: {reverse_string(example2)}")
    print()
    
    # Example 3: User input
    user_input = input("Enter a string to reverse: ")
    print(f"Reversed: {reverse_string(user_input)}")


if __name__ == "__main__":
    main()