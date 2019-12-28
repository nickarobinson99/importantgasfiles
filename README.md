# importantgasfiles

The important shit you are probably looking for for the charting would be in app1.py and in templates/index.html

in app1.py "chart_data()" is the important function. This is where the weird generator function shit plays in

Looking at it now, it looks like i wrote it such that it should just work. chart_data loops through all of the possible channels
and plots the data from that channel. grab_voltage should first try to pull data from the channel but i would remove the except:
statement where it generates a random number.
