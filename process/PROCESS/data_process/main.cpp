// main.cpp

#include <iostream>
#include "file_read.h"
#include "data_process.h"
#include "file_write.h"

int main() {
    std::cout << "Main program is running" << std::endl;

    // 调用 file_read.cpp 中的file_read
    std::string input;
    //std::cout << "before read \n" << std::endl;

    input = file_read();
    //std::cout << "Fileread success \n" << std::endl; 

    // 调用 data_process.cpp 的data_process
    std::string output = data_process(input);

    // 调用 file_write.cpp 的 file_write, 数据写入
    file_write(output);

    std::cout << "Finish running" << std::endl;

    return 0;
}
