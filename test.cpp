#include <dlfcn.h>
#include <iostream>
#include "libGameLogic.h"
#include "commonUtils.h"
#include <string>

Player* globalPlayer = NULL;

void World::Tick(float f)
{
  ClientWorld* world = *((ClientWorld* *) dlsym(RTLD_NEXT, "GameWorld"));
  IPlayer* iPlayer = world->m_activePlayer.m_object;
  Player* player = ((Player*) iPlayer);
  player->m_walkingSpeed = 9999;
  player->m_jumpHoldTime = 0.3;
  player->m_jumpSpeed = 2000;
  globalPlayer = player;
}


//SP 10.0,10.0,10.0
//tz 10.0
//GT
void Player::Chat(const char * msg){  
  //std::cout << "IsPlayer():" << this->IsPlayer() << std::endl;
  //std::cout << "GetPlayerName():" << this->GetPlayerName() << std::endl;
  //std::cout << "message:" << msg << std::endl;
  
  std::string message (msg);
  if( message.substr(0, 2) == "GP" )
  {
    Vector3 curLoc = this->GetPosition();
    std::cout << "GetPosition(): (" << curLoc.x << "," << curLoc.y << "," << curLoc.z << ")" << std::endl;
  } 
  else if( message.substr(0, 2) == "SP" )
  {
    std::shared_ptr<std::vector<std::string>> results = commonUtils::ParseString(message, "[0-9.-]+");

    float x = std::stof( results->at(0) );
    float y = std::stof( results->at(1) );
    float z = std::stof( results->at(2) );
    Vector3 newPos (x, y, z);
    
    std::cout << "setting location to: (" << newPos.x << "," << newPos.y << "," << newPos.z << ")" << std::endl;
    this->SetPosition(newPos);
  }
  
}

bool Player::CanJump()
{
  return true;
}

int main() 
{
	
}
