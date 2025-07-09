"""
Troy Playground - Execute functions and extract their local variables

A debugging tool that allows you to run functions and extract their local 
variables for inspection, effectively turning any function into a playground.
"""

from .core import extract_locals, run_function_playground

__version__ = "0.1.0"
__all__ = ["extract_locals", "run_function_playground"]