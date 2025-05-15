import pytodotxt, argparse

parser = argparse.ArgumentParser()
parser.add_argument("todotxt", help="location of todo.txt file")
args = parser.parse_args()

print(args)
