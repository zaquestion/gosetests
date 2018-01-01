gosetests
==

*Not yet usable*

`gosetests` is a tool for iteratively converting blackbox [nose](https://nose.readthedocs.io/en/latest/) style tests (python) into GoLang tests. It will be used to convert a 300+ integration test suite. As such it relies on your tests having no knowledge of the code its testing. For instances, the tests this tool is being built against send http requests and assert on the responses / side effects.

## The Idea

- build out a system for converting python primitives (variables, definitions, etc) into golang equivalents
- Create a configuration scheme for mapping a piece of python code to GoLang code
  - This is really the key to the system working, I imagine if this projects go far enough that a configuration file would continue to grow over time with python -> GoLang conversions and could start to be more broadly applied.
  - handle mapping function calls, unhandled function calls would be stubbed out in code and configuration updated to call said stub. Then you would manually write the function
  - ideal: handle mapping python patterns into GoLang patterns
