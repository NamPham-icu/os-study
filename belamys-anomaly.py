#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 23:27:29 2025

@author: nampham
"""
import numpy as np
import matplotlib.pyplot as plt

def fifo_page_faults(pages, frame_count):
    memory = []
    page_faults = 0
    memory_states = []
    fault_infos = []

    for page in pages:
        info = ""
        if page not in memory:
            page_faults += 1
            if len(memory) < frame_count:
                memory.append(page)
                info = f"{page} in"
            else:
                evicted = memory.pop(0)
                memory.append(page)
                info = f"{page} in ({evicted} out)"
        else:
            info = ""
        memory_states.append(memory.copy())
        fault_infos.append(info)
    return page_faults, memory_states, fault_infos

# Input Settings
original_sequence = [0, 4, 2, 3, 1, 0, 2, 1, 3, 0, 4, 2, 3, 1, 0, 4, 2, 3]
frame_sizes_mapped = [3, 4, 5, 6]

# Record Data
fault_counts_mapped = {}
for frame_count in frame_sizes_mapped:
    faults, _, _ = fifo_page_faults(original_sequence, frame_count)
    fault_counts_mapped[frame_count] = faults

# Plotting
plt.figure(figsize=(10, 5))
plt.bar(fault_counts_mapped.keys(), fault_counts_mapped.values(), width=0.6)
plt.xlabel("Page Number")
plt.ylabel("Page Faults")
plt.title("FIFO Page Replacement")
plt.grid(axis='y')
plt.xticks(frame_sizes_mapped)
plt.show()
