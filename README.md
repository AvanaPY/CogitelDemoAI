# Cogitel AI System Demo

This program creates a normally distributed dataset and trains an AI on it. 
The data has a mean of `25` and a standard deviation of `2.2`, all values under `22` or above `28` are considered "bad" values, all others are "good" values. 

After the AI has been trained it creates a set of 100 numbers that are normally distributed that follow the same "good-value-bad-value" rules and tests the AI on it. 

It reaches roughly `99.9%` accuracy.