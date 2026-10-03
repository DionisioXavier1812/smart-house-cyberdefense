# Ambiente 3 – Assistente de Voz Abusado

## Sobre o Cenário
Assistente de voz integrado ao hub IoT, com comandos críticos habilitados.

## Arquitetura
Hub IoT ? Voice Assistant ? IoT Devices

## Cadeia de Ataque
1. Comprometimento da conta
2. Execução de comando malicioso
3. Pivoting para outros dispositivos

## Incidente
Atacante executou comandos sensíveis via voz.

## Impacto
Controle indevido de dispositivos IoT.

## Logs Simulados
Oct 03 11:24:02 assistant-voice event: Command executed: "unlock front door"

## IoCs
Comando: unlock front door
User-Agent: VoiceAPI/3.2
Hash: 8a1c9fbbd2e3f1a9c4e8d1f2b9a7c3e1

## MITRE ATT&CK
T1041 – Exfiltration
T1059 – Command Execution

## Timeline DFIR
11:24 – Comando malicioso
11:25 – Evento no hub

## Evidências
voice.log
hub-events.log

## Análise
Assistente executou comandos críticos sem validação.

## Conclusão
Comandos críticos devem exigir confirmação.

## Recomendações
Hardening IoT
MFA
Alertas de voz
