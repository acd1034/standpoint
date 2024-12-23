cmake_minimum_required(VERSION 3.18)
project(my_package)

# nanobind を利用
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
find_package(nanobind CONFIG REQUIRED)

# Python モジュール用ライブラリを定義
nanobind_add_module(math src/math.cpp)
