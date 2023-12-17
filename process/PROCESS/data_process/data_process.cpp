// data_process.cpp

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

std::string data_process(const std::string& input){
    std::istringstream iss(input);
    std::string result;
    //S=V*V/2gμ（g=9.8m/s2） v速度，g重力加速度, μ摩擦系数 = 0.75
    //输入 -> 速度 距离1 距离2 距离3
    int current_speed, distance_num, avg_distance, num, actural_length, counter, distance;
    counter = 0; //计数器
    distance_num = 0;
    iss >> current_speed;
    while (iss >> num) {
        distance_num += num;
        counter ++;
    }
    if(counter != 3){
        result = "ERROR传感器错误";
        return result;
    }
    distance = current_speed * current_speed / (2 * 0.75 * 9.8);
    distance++;
    avg_distance = distance_num / 3; //实际距离
    actural_length = (2 * current_speed) +  distance; //刹车需要的距离
    
    //std::cout << "MARKDEP " << actural_length << std::endl;
    if(actural_length >= avg_distance){ //要撞了！
        result += "要撞了! \n";
    }
    else{
        result += "安全距离 \n";
    }
    result += "距离：";
    std::string str = std::to_string(avg_distance);
    result += str;
    result += " \n";
    result += "刹车最短距离： ";
    std::string str2 = std::to_string(actural_length);
    result += str2;
    result += " \n";

    return result;
}