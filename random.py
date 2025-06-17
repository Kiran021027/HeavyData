#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

def generate_random_string(length=8):
    """Generate a random alphanumeric string."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

# Example usage
if __name__ == "__main__":
    print(generate_random_string(10))  # Example: 'aB3dE7fG1H'
    print(is_even(4))  # True
    print(is_even(7))  # False

