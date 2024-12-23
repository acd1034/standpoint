#include <nanobind/nanobind.h>
#include <nanobind/stl.h>

namespace nb = nanobind;

constexpr auto divmod(double a, double b) -> std::pair<double, double>
{
    return {a / b, a % b};
}

NB_MODULE(my_module, m)
{
    m.doc() = "An example math module using nanobind";

    m.def("divmod", divmod, "Divide and modulo two numbers");
}
