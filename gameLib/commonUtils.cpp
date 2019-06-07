#include "commonUtils.h"

std::shared_ptr<std::vector<std::string>> commonUtils::ParseString(std::string input, std::string regex)
{
  std::regex word_regex(regex);

  std::sregex_iterator result_begin = std::sregex_iterator(input.begin(), input.end(), word_regex);
  std::sregex_iterator result_end = std::sregex_iterator();

  std::shared_ptr<std::vector<std::string>> results = std::shared_ptr<std::vector<std::string>>( new std::vector<std::string>( ) );
  for(std::sregex_iterator i = result_begin; i != result_end; ++i)
  {
    std::smatch match = *i;
    std::string match_str = match.str();
    results->push_back( match_str );
  }

  std::cout << "size:" << results->size() << std::endl;
  for(int i = 0; i < results->size(); ++i)
  {
     std::cout << "at(" << i << "):" << results->at(i) << std::endl;
  }

  return results;
}
