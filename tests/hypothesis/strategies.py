from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy


def integers_with_exclude(min_value=0, max_value=1000, exclude=None) -> SearchStrategy:
    if exclude:
        allowed_values = [value for value in range(min_value, max_value+1) if value not in exclude]
        return st.sampled_from(allowed_values)
    else:
        return st.integers(min_value=min_value, max_value=max_value)
