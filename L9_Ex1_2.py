from time import sleep

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        try:
            while True:
                print(TrafficLight.__color[i % 3])
                if i % 3 == 0:
                    sleep(7)
                elif i % 3 == 1:
                    sleep(2)
                elif i % 3 == 2:
                    sleep(5)
                i += 1
        except KeyboardInterrupt:
            print('Stopped')

cycle = TrafficLight()
cycle.running()
