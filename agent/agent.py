class Agent:
    """
    Primary reasoning agent.
    Proposes next action based on screened state.
    """

    def decide(self, state_view):
        raise NotImplementedError("Agent decision logic not implemented")
