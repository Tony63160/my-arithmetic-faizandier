# SPDX-FileCopyrightText: 2024-present tony <anthony.faizandier@etu.uca.fr>
#
# SPDX-License-Identifier: MIT


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

