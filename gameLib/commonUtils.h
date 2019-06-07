#ifndef COMMON_UTILS
#define COMMON_UTILS

#include <vector>
#include <string>
#include <regex>
#include <iterator>
#include <iostream>
#include <memory>


class commonUtils
{
  public:
  static std::shared_ptr<std::vector<std::string>> ParseString(std::string input, std::string regex);
};

#endif
