"""Execute the documented adaptations, without the original repositories."""

import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEVELOP = ROOT / "skills/tomi-coder-develop/references/code-examples.md"
CONSTRUCT = ROOT / "skills/tomi-code-construct/references/review-example.md"
PREPARE = ROOT / "skills/tomi-coder-prepare/references/tdd-example.md"


def snippet(path, name):
    pattern = rf"<!-- snippet: {re.escape(name)} -->\s*```\w+\n(.*?)\n```"
    match = re.search(pattern, path.read_text(encoding="utf-8"), re.S)
    if match is None:
        raise AssertionError(f"Missing executable example: {name}")
    return match[1]


class CodeExamplesTests(unittest.TestCase):
    def test_prepare_example_reaches_red_then_green(self):
        lua = shutil.which("lua")
        if lua is None:
            self.skipTest("lua is unavailable; TDD example not verified")
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            test = folder / "test_group.lua"
            module = folder / "group.lua"
            test.write_text(snippet(PREPARE, "contract-test"), encoding="utf-8")
            module.write_text(snippet(PREPARE, "red-stub"), encoding="utf-8")
            red = subprocess.run([lua, str(test)], cwd=folder, capture_output=True, text=True, timeout=30)
            self.assertEqual(red.returncode, 1)
            self.assertIn("assertion failed", red.stderr)
            module.write_text(snippet(DEVELOP, "state"), encoding="utf-8")
            green = subprocess.run([lua, str(test)], cwd=folder, capture_output=True, text=True, timeout=30)
            self.assertEqual(green.returncode, 0, green.stderr)

    def execute(self, tool, code, suffix, flags=()):
        executable = shutil.which(tool)
        if executable is None:
            self.skipTest(f"{tool} is unavailable; example not verified")
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / ("Demo.java" if tool == "javac" else "demo" + suffix)
            source.write_text(code, encoding="utf-8")
            if tool == "lua":
                commands = [[executable, str(source)]]
            elif tool == "javac":
                java = shutil.which("java")
                if java is None:
                    self.skipTest("java is unavailable; example not verified")
                commands = [[executable, str(source)], [java, "-ea", "-cp", directory, "Demo"]]
            else:
                binary = str(Path(directory) / "demo")
                commands = [[executable, *flags, str(source), "-o", binary], [binary]]
            for command in commands:
                result = subprocess.run(command, cwd=directory, capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def lua_module(self, name, assertions):
        code = "local sample = (function()\n" + snippet(DEVELOP, name) + "\nend)()\n"
        self.execute("lua", code + assertions, ".lua")

    def test_state_and_bounds(self):
        self.lua_module("state", '''
local a, b = sample:new(), sample:new()
a:append("alpha")
a:append("beta")
assert(a.size == 2 and b.size == 0)
assert(a:at(1) == "alpha" and a:at(2) == "beta")
assert(not pcall(function() a:at(0) end))
assert(not pcall(function() a:at(3) end))
assert(not pcall(function() b:at(1) end))
assert(a.items ~= b.items)
''')

    def test_recursive_copy_and_reuse(self):
        self.lua_module("reuse", '''
local metadata = {tag = {value = "plain"}}
local original = setmetatable({{score = 3}, {score = 8}}, metadata)
local copy = sample.copy(original)
copy[1].score = 99
assert(original[1].score == 3)
assert(getmetatable(copy) ~= metadata)
getmetatable(copy).tag.value = "changed"
assert(metadata.tag.value == "plain")
assert(sample.copy(7) == 7)
local key = {label = "key"}
local keyed = sample.copy({[key] = "value"})
local copied_key, value = next(keyed)
assert(copied_key ~= key and copied_key.label == "key" and value == "value")
local empty = {}; assert(next(sample.copy(empty)) == nil)
''')

    def test_search_and_state_change(self):
        code = snippet(DEVELOP, "search") + '''
#include <assert.h>
int main(void) {
    Entry second = {"beta", 0, NULL};
    Entry first = {"alpha", 0, &second};
    Catalog catalog = {&first};
    assert(find_entry(&catalog, "beta") == &second);
    assert(mark_entry(&catalog, "beta") == 1);
    assert(second.marked == 1 && first.marked == 0);
    assert(mark_entry(&catalog, "absent") == 0);
    Catalog empty = {NULL};
    assert(find_entry(&empty, "alpha") == NULL);
}
'''
        self.execute("gcc", code, ".c", ("-std=c11", "-Wall", "-Wextra", "-Werror"))

    def test_construct_and_append_values(self):
        code = snippet(DEVELOP, "decisions") + '''
#include <cassert>
int main() {
    Sequence sequence = {};
    assert(append_step(sequence, 'a', 2));
    assert(append_step(sequence, 'b', 4));
    assert(sequence.size == 2);
    assert(sequence.steps[0].direction == 'a' && sequence.steps[0].count == 2);
    assert(sequence.steps[1].direction == 'b' && sequence.steps[1].count == 4);
    assert(append_step(sequence, 'c', 1));
    assert(append_step(sequence, 'd', 3));
    assert(!append_step(sequence, 'e', 9));
    assert(sequence.size == 4 && sequence.steps[3].direction == 'd');
}
'''
        self.execute("g++", code, ".cpp", ("-std=c++14", "-Wall", "-Wextra", "-Werror"))

    def test_execution_and_callback(self):
        self.lua_module("callback", '''
assert(sample.run(nil) == nil)
assert(sample.run(function() end) == true)
assert(sample.run(function() return 0 end) == 0)
local output = {set = function(self, value) self.value = value end}
sample.on_action(function() return "answer" end, output)
assert(output.value == "answer")
sample.on_action(nil, output)
assert(output.value == "error")
sample.on_action(function() return false end, output)
assert(output.value == "error")
''')

    def test_ui_delegation(self):
        code = snippet(DEVELOP, "delegation") + '''
class Screens {
    static int calls;
    static void showList() { calls++; }
}
public class Demo {
    public static void main(String[] args) {
        new PanelActions().openList();
        assert Screens.calls == 1;
    }
}
'''
        self.execute("javac", code, ".java")

    def test_review_handles_absent_container_before_access(self):
        code = snippet(CONSTRUCT, "fixed-search") + '''
#include <assert.h>
int main(void) {
    assert(find_entry(NULL, "alpha") == NULL);
    Catalog empty = {NULL};
    assert(find_entry(&empty, "alpha") == NULL);
    Entry item = {"alpha", NULL};
    Catalog full = {&item};
    assert(find_entry(&full, "alpha") == &item);
    assert(find_entry(&full, "absent") == NULL);
}
'''
        self.execute("gcc", code, ".c", ("-std=c11", "-Wall", "-Wextra", "-Werror"))
