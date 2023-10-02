"""Executes a query while measuring execution time"""

import time


def measure_execution_time(session, query):
    """Executes a query while measuring execution time"""
    start = time.time()
    result = session.execute(query)
    end = time.time()

    return result, end-start
