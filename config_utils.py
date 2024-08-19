import os


def list_env_var(variable_name: str) -> list:
    """
    Enumerates Environment Variables starting with a given prefix and a self-incrementing index as postfix.
    Addressing/Counting begins at zero, because we're not morons, but real IT people (sorry Matlab folks).
    Enumeration stops when no value for an Environment Variable at an index is found. The previously found
    values will be returned in the form  of a list. An empty list is returned in case nothing was found.

    Here are example environment variables:
    - EXAMPLE_VAR__0
    - EXAMPLE_VAR__1

    You can get a list containing EXAMPLE_VAR__0 and EXAMPLE_VAR__1 if you call `list_env_var('EXAMPLE_VAR')`.
    """
    current_index = 0
    found_api_keys = []

    while True:
        env_var_value = os.environ.get(f'{variable_name}__{current_index}', None)
        if env_var_value is None:
            return found_api_keys

        found_api_keys.append(env_var_value)
        current_index += 1
