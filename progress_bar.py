import sys, time

for i in range(5):
    sys.stdout.write('{0}/5\r'.format(i + 1))
    sys.stdout.flush()
    time.sleep(1)