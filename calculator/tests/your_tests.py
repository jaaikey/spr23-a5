#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

# Checks that the program outputs "20" for an input of "4 * 5"
assert run("4 * 5").output == "20"
# Checks that the program fails (correctly errors) for input "5 ^ 6"
assert run("5 ^ 6").exit_status != 0

print("All tests passed!")
