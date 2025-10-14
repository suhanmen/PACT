from datasets import load_dataset

def load_section():
    use_section = [
            "boundary_and_edge_case", 
            "complex_corner_case", 
            "performance_stress_case", 
            "logic_coverage", 
            "functional_path_coverage"
            ]
    
    return use_section


def load_data(dataset_name):
    if dataset_name == 'humaneval': # 164 problems
        return load_dataset("openai/openai_humaneval")
    elif dataset_name == 'mbpp_full': # 974 problems
        return load_dataset("Muennighoff/mbpp", "full")
    elif dataset_name == 'mbpp_sanitized': # 427 problems
        return load_dataset("Muennighoff/mbpp", "sanitized")
    elif dataset_name == 'mbpp_plus': # 378 problems (use a subset of hand-verified problems from MBPP-)
        return load_dataset("evalplus/mbppplus")
    else:
        raise NotImplementedError(f"Dataset {dataset_name} not implemented yet.")