# SluG
Systems Leaker with User Gratitude 

## What is SluG

## Architecture
- Control center
  - Dashboard
- Agent
  - Dirty work
- Server
  - Central information hub
- Toolbox
  - generateId
    - input: n/a
    - output: unique id
    - description: this function generates an unique identifier for an agent
  - getGeoInfo
    - input: n/a
    - output: geo coordinates
    - description: this function gets the geographical coordinates from the agent
  - getFilesNumber
    - input: n/a
    - output: number of files
    - description: this function returns the number of objective files in the target folders

## Data model
- Agent
  - id
  - geoinfo
  - filesnumber

## Functional requirements
- Start contact with the server
- Encrypt a set of files in different directories depending on the OS
  - Windows
  - Linux
  - Mac
- Provide information about the encryption process to the server
- Monitoring and alerting processes
- Payment message
- Decrypt process

## Comments
