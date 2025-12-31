def execute_code(code: str, tests: list):
    """
    Executes code against tests.
    Executor is the ONLY oracle.
    """
    try:
        exec_globals = {}
        exec(code, exec_globals)
    except Exception as e:
        return {"passed": False, "error": str(e)}

    fn = list(exec_globals.values())[-1]

    for test in tests:
        try:
            output = fn(*test.inputs)
            if test.assertion_type == "exact":
                if output != test.expected:
                    return {"passed": False, "error": "Assertion failed"}
        except Exception as e:
            return {"passed": False, "error": str(e)}

    return {"passed": True, "error": None}
