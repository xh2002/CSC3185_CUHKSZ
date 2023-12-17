// file_write.cpp

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

void file_write(const std::string& output){
    // 打开文件流，并指定写入模式（std::ios::out）
    std::string filePath = "..\\data\\output.txt";
    std::ofstream outputFile(filePath, std::ios::out);

    // 检查文件是否成功打开
    if (!outputFile.is_open()) {
        std::cerr << "Can't open output file" << std::endl;
        //return 1;
    }
    
    // 写入
    outputFile << output << std::endl;

    // 关闭文件
    outputFile.close();
}
