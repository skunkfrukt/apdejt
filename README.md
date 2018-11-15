# apdejt

A simple function that uses pip to install the dependencies of an application.

## Usage
```python
import apdejt

# Look for requirements in a specified directory:
apdejt.install_dependencties(".")

# Or, supply the whole path to requirements.txt explicitly.
apdejt.install_dependencies("my_application/requirements.txt")

# Or, look for requirements.txt in the same directory as another file,
# such as __file__.
apdejt.install_dependencies(__file__)
```

## Example
```python
import argparse
import apdejt

def take_over_the_world():
    pass  # TODO

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--install_dependencies",
        dest="install_dependencies",
        action="store_true"
    )
    args = parser.parse_args()

    if args.install_dependencies:
        apdejt.install_dependencies(__file__)
    else:
        import my_thing
        
        my_thing.do_the_thing(args)
```
