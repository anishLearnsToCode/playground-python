class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, character: str) -> None:
        self.stack.append(character)

    def enqueueCharacter(self, character: str) -> None:
        self.queue.append(character)

    def popCharacter(self) -> str:
        return self.stack.pop()

    def dequeueCharacter(self) -> str:
        return self.queue.pop(0)
