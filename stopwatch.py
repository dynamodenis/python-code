import time

print('Press Enter to start the Stopwatch')
print('and, press CTRL + C  to stop the stopwatch')

while True:
    try:
        input()
        start_time = time.time()
        print('Stop watch started..')
        
    except KeyboardInterrupt:
        print('Stopwatch stopped..')
        end_time = time.time()
        print("The totaltime", round(end_time-start_time,2),"seconds")
        break