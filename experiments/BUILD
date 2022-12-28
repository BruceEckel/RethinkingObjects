python_sources(
    name="lib",
)

pex_binary(
    name="app",
    entry_point="experiments.a:app",
    dependencies=[
        ":lib",
    ],
)

python_tests(
    name="tests",
    sources=["*.py", "!__init__.py"],
)
