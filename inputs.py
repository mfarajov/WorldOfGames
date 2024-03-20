import os


def get_input(env_var, prompt, cast_type=str):
    value = os.getenv(env_var)
    if value is None:
        value = input(prompt)
    return cast_type(value)
