"""
    Title: measures_utils.py

    Author: Ashley Williams

    Description: A collection of generic utility functions that are used
    throughout coast by various modules relating to the reporting and
    performance measures.
"""
import sys


def draw_progress_bar(percent, bar_len=20):
    """
        Given a percentage, will print a progress bar to the console. Useful
        for reporting progress on large calculations.

        Args:
            percent: The percent of the calculation that is complete.
            bar_len: How long the progress bar that is displayed should be.
                     Default is 20 characters.

        Returns:
            Nothing, output is printed to the stdout.
    """
    sys.stdout.write("\r")
    progress = ""
    for i in range(bar_len):
        if i < int(bar_len * percent):
            progress += "="
        else:
            progress += " "
    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
    sys.stdout.flush()
