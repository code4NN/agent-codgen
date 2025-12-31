class RunMemory:
    """
    Tracks failed hypotheses within a single run.
    """

    def __init__(self):
        self.failed = set()

    def add(self, hypothesis: str):
        self.failed.add(hypothesis)

    def seen(self, hypothesis: str) -> bool:
        return hypothesis in self.failed
