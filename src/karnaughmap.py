#!/bin/python3

# Import

from lib2to3.pgen2 import driver
from struct import unpack
from traceback import print_tb
from typing import Iterable
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from main import TRUTH_TABLE_OUT


def map_cell(binary: Iterable[bool], n=5) -> tuple[int]:
    x_len = int(2**((n+n % 2)/2))
    y_len = int(2**((n+n % 2)/2)/(1+n % 2))
    x = set(range(x_len))
    y = set(range(y_len))

    # GAMBIARRA (fds, vai ser 5 mesmo)
    # bit 0:
    x &= ({0, 3, 4, 7}, {1, 2, 5, 6})[binary[-1]]
    # bit 1:
    y &= ({0, 3}, {1, 2})[binary[-2]]
    # bit 2:
    x &= ({0, 1, 6, 7}, {2, 3, 4, 5})[binary[-3]]
    # bit 3:
    y &= ({0, 1}, {2, 3})[binary[-4]]
    # bit 4:
    x &= ({0, 1, 2, 3}, {4, 5, 6, 7})[binary[-5]]

    if (len(x), len(y)) != (1, 1):
        raise Exception("Karnaugh of Schrödinger")

    return (list(x)[0], list(y)[0])


def cell_xpath(column: int, line: int) -> str:
    return f"//*[name()='text' and @x='{column*40+61}' and @y={line*40+98}]"


def equation_formatting(eq: str) -> str:
    eq = eq.removeprefix("y = ")
    eq = eq.replace("x̄", "!x")
    eq = eq.replace("x4", "a ")
    eq = eq.replace("x3", "b ")
    eq = eq.replace("x2", "c ")
    eq = eq.replace("x1", "d ")
    eq = eq.replace("x0", "e ")
    eq = eq.replace(" )", ")")
    eq = eq.replace("∨", "+")
    return eq


def open_web_page():
    # Setup webdriver
    KV_HOST = "https://www.mathematik.uni-marburg.de/~thormae/lectures/ti1/code/karnaughmap/index.html"
    driver = webdriver.Firefox()
    driver.get(KV_HOST)

    # Check the site name
    assert "Karnaugh-Veitch Map" in driver.title

    # Set number of inputs
    input_num_elem = driver.find_element(By.ID, "noOfVarsChanged_id")
    input_num_elem.send_keys(Keys.ARROW_DOWN)

    return driver


if __name__ == '__main__':
    equations = []
    for segment_index in range(8):
        print("Segment", segment_index)
        with open_web_page() as driver:
            for seven_segments, binary in TRUTH_TABLE_OUT.items():
                if seven_segments[segment_index]:
                    cell = driver.find_element(
                        By.XPATH, cell_xpath(*map_cell(binary)))
                    print(f"{cell.text} == {binary}")
                    cell.click()
            output = driver.find_elements(By.CLASS_NAME, "qmcMathFont")
            print(output[1].text)
            equations.append(output[1].text+'\n')
            driver.close

    equations = list(map(equation_formatting, equations))
    print(*equations)

    with open('../bin2seg.txt', 'w') as save_file:
        save_file.writelines(equations)
