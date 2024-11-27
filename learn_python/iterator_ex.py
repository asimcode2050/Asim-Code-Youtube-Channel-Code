
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start  # Return the current countdown value.


countdown = CountDown(5)
for num in countdown:
    print(num)  # Print each countdown number.
