"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
"""


import colorsys

def rgb_to_hsv(r, g, b):
    # Normalize the RGB values by scaling them to be between 0 and 1
    r_normalized = r / 255.0
    g_normalized = g / 255.0
    b_normalized = b / 255.0

    # Convert the normalized RGB values to HSV values
    h, s, v = colorsys.rgb_to_hsv(r_normalized, g_normalized, b_normalized)

    # Scale the HSV values to be between 0 and 100 for S and V, and 0 to 360 for H
    h_scaled = int(h * 360)
    s_scaled = round(s * 100, 1)
    v_scaled = round(v * 100, 1)

    return h_scaled, s_scaled, v_scaled
