# FlatMountain2D
2D Multiplayer framework with focus on simplicity

This framework aims to create a simple and easy to use basis for multiplayer games.
To accomplish this the project makes use of following concepts:\
1. __Client/Server model__: Users interact with a Displayclient witch connects the game(engine/server).\
    1.1. The __DisplayClient__: Collects user input and displays grafics and plays sounds.\
    1.2. The __GameServer__ collects inputs from the clients, feeds the simultaion/game with them and sends rendering-data back.\
2. The simulation uses a entity-component-system inspired approche.\
    2.1. All the games (state)data is organized inside the __Context__ class.\ This class is later used by all other components to perform operations on data. The Context class manages following data structures:\
        2.1.1. __Component__: stores data of entitys eg.: a health component may store hp and a armor component stores type and strength.\
        2.1.2. __Entity__: Combines multible components to represent an "object" in the game like a knight, tree, cow, troll etc...\
        2.1.3. __Config__: Stores configuration stored in files. Also contains global data.\
    2.2 Operations on the context(s) are performed by Systems and Services.\
        2.2.1. __System__: Runs on certain conditions based on time or events. changes/creates/removes game data.\
        2.2.2. __Service__: Used by systems, other services or the engine. Accesses gamedata and provides ways for events and communication.\
