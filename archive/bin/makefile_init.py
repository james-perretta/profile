#! /usr/bin/env python

import argparse


def main():
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("")

    return parser.parse_args()


MAKEFILE_DEFAULTS = {
    'CXX': 'g++',
    'CXXFLAGS'
}


MAKEFILE_TEMPLATE = """CXX = g++

CXXFLAGS = -Wall -pedantic -Wextra --std=c++11 -c
CPPFLAGS = -Isrc -MMD -MP

LD = $(CXX)
LDFLAGS = -Wall

src_dir = {src_dir}
lib_dir = {lib_dir}
testcases_dir = testcases
build_dir = build

src_files = $(wildcard $(src_dir)/*.cpp)
src_objs = $(src_files:%.cpp=$(build_dir)/%.o)
exe = pager

testcase_mains = $(wildcard $(testcases_dir)/*.cc)
testcase_objs = $(testcase_mains:$(testcases_dir)/%.cc=$(build_dir)/$(testcases_dir)/%.o)
testcase_exes = $(testcase_objs:.o=.exe)

debug: CXXFLAGS += -g
release: CPPFLAGS += -DNDEBUG
debug release: $(exe) $(testcase_exes)

$(build_dir)/$(src_dir)/%.o: $(src_dir)/%.cpp
    mkdir -p $(dir $@)
    $(CXX) $(CXXFLAGS) $(CPPFLAGS) $< -o $@

$(exe): $(src_objs)
    $(LD) $(LDFLAGS) $(lib_dir)/libvm_pager.a $^ -o $@

# Test case targets
$(build_dir)/$(testcases_dir)/%.o: $(testcases_dir)/%.cc
    mkdir -p $(dir $@)
    $(CXX) $(CXXFLAGS) $(CPPFLAGS) $< -o $@

$(build_dir)/$(testcases_dir)/%.exe: $(build_dir)/$(testcases_dir)/%.o
    $(LD) $(LDFLAGS) -ldl $^ $(lib_dir)/libvm_app.a -o $@

-include $(build_dir)/*/*.d

.SECONDARY:

.PHONY: clean
clean:
    rm -rf $(build_dir) $(exe)
"""


if __name__ == '__main__':
    main()
