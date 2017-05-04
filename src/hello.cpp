#include "hello.hpp"
#include <iostream>
#include <vector>
#include <cstddef>

namespace example {

void hello_world(int *buf, size_t buf_size) {
    std::cout << "Hello C++ World!\n";

    for (int i = 0; i < buf_size; i++) {
        std::cout << buf[i] << "\n";
    }
}

}   /* namespace example */
