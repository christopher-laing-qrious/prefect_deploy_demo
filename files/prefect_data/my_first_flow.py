from prefect import flow, task
import time

@task
def print_hello(name):
    time.sleep(5)  # Simulate some work
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

@flow
def hello_flow(name: str = "World"):
    result = print_hello(name)
    print(f"Flow result: {result}")

if __name__ == "__main__":
    hello_flow("Prefect")
