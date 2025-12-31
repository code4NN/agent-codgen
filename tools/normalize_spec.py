def normalize_spec(spec):
    """
    Validates and locks the problem specification.
    """
    if spec.confidence < 0.75:
        raise ValueError("Low confidence problem spec")

    for amb in spec.ambiguities:
        if amb.blocking:
            raise ValueError("Blocking ambiguity unresolved")

    return spec
