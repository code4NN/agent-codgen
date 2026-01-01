from contracts.problem_spec import ProblemSpec, Argument, Ambiguity

def parse_problem(problem_text: str) -> ProblemSpec:
    return ProblemSpec(
        function_name="twoSum",
        inputs=[
            Argument(name="nums", type="List[int]"),
            Argument(name="target", type="int"),
        ],
        output_type="List[int]",
        input_mode="positional",
        multiple_valid_outputs=True,
        edge_cases=["duplicate_values"],
        ambiguities=[
            Ambiguity(
                description="Multiple valid index pairs possible",
                options=["return any valid pair"],
                default="return any valid pair",
                blocking=False,
            )
        ],
        confidence=0.95,
    )
