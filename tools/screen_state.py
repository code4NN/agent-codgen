def screen_state(global_state):
    """
    Produce a reduced, relevant view of state for the agent.
    Does NOT mutate global state.
    """
    return {
        "controller_state": global_state.get("controller_state"),
        "locked_spec": global_state.get("problem_spec"),
        "last_error": global_state.get("last_error"),
        "failed_hypotheses": list(global_state.get("failed_hypotheses", []))
    }
