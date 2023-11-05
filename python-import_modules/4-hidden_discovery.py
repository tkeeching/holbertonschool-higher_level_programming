#!/usr/bin/env python
import hidden_4

if __name__ == "__main__":
    keys = hidden_4.__dir__()
    print(keys)
    for i in range(0, len(keys)):
        if (keys[i][0] != '_'):
            print(keys[i])
