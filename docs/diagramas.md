# Diagramas

## Rede Doméstica
graph TD
    Internet --> Router
    Router --> IoT
    Router --> Users
    IoT --> Camera
    IoT --> SmartLock
    IoT --> VoiceAssistant

## Fluxo de Ataque
sequenceDiagram
    attacker->>camera: brute force
    camera->>hub: config change
    attacker->>smartlock: unlock
    attacker->>assistant: malicious command

## Arquitetura IoT
flowchart LR
    Hub --> Camera
    Hub --> SmartLock
    Hub --> Sensors
    Hub --> VoiceAssistant
