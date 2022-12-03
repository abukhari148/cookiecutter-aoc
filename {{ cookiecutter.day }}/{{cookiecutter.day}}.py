from datetime import date
from aocd import submit
from aocd.models import Puzzle

day, year = date.today().day, date.today().year
p = Puzzle(day=day, year=year)


def p1(data):
    """Solve part 1."""


def p2(data):
    """Solve part 2."""


submit(p1(p.input_data), part="a", day=day, year=year)
submit(p2(p.input_data), part="b", day=day, year=year)
