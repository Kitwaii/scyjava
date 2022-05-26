import unittest


def print_problems(problems):
    for method_name, trace in problems:
        print(method_name)
        print(trace)


loader = unittest.loader.TestLoader()
suite = loader.discover('tests')
result = unittest.TestResult()
suite.run(result)

print(f"Success? {result.wasSuccessful()}")
print(f"Total tests run = {result.testsRun}")

if len(result.failures) > 0:
    print()
    print("[Failures]")
    print_problems(result.failures)
if len(result.errors) > 0:
    print()
    print("[Errors]")
    print_problems(result.errors)
