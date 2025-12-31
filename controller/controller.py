class Controller:
    """
    Enforces iteration bounds, hypothesis uniqueness,
    and action validity. Does NOT reason.
    """

    def __init__(self, max_iterations=3):
        self.iteration = 0
        self.used_hypotheses = set()
        self.max_iterations = max_iterations

    def allow(self, action):
        if action.hypothesis in self.used_hypotheses:
            return False, "Repeated hypothesis"
        if self.iteration >= self.max_iterations:
            return False, "Iteration limit reached"
        return True, "Approved"

    def register(self, action):
        self.used_hypotheses.add(action.hypothesis)
        self.iteration += 1
