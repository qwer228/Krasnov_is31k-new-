class Timer:
    __slots__ = ('start', 'end')
    
    def __init__(self, start, end):
        self.start = start  # в секундах
        self.end = end
    
    def duration(self):
        return max(0, self.end - self.start)

timer = Timer(100, 250)
print(f"Длительность: {timer.duration()} сек.")

