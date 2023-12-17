#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

std::string file_read() {
    // 打开输入文件
    std::ifstream inputFile("..\\data\\input.txt");
    // 检查文件是否成功打开
    if (!inputFile.is_open()) {
        std::cerr << "Can't open input file" << std::endl;
        //return 1;
    }

    // 逐行读取输入文件，改成string
    std::stringstream buffer;
    buffer << inputFile.rdbuf();
    std::string input = buffer.str();
    //std::cout << "read result = " << input << std::endl;
    
    // 关闭文件
    inputFile.close();

    return input;
}