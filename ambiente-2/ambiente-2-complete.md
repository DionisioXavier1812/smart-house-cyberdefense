# Ambiente 2 – Smart Lock Intrusão Remota

## Sobre o Cenário
Fechadura inteligente controlada via app, sem MFA e com API exposta.

## Arquitetura
IoT VLAN ? SmartLock ? Hub IoT ? Cloud API

## Cadeia de Ataque
1. Enumeração da API  
2. Descoberta de endpoint /unlock  
3. Uso de credenciais fracas  
4. Unlock remoto  

## Incidente
Atacante destravou a porta remotamente.

## Impacto
Risco físico e invasão domiciliar.

## Logs Simulados
Oct 03 11:23:44 smartlock: Remote unlock by 201.55.19.77  

## IoCs
IP: 201.55.19.77  
URI: /unlock  
User-Agent: "Python-requests/2.31"  
Hash suspeito: 7c9a1fbbd2e3f1a9c4e8d1f2b9a7c3e1  

## MITRE ATT&CK
T1021 – Remote Services  
T1059 – Command Execution  

## Timeline DFIR
11:23 – Unlock remoto  
11:24 – Notificação no hub  

## Evidências
- smartlock.log  
- API access log  

## Playbook
1. Desativar controle remoto  
2. Resetar credenciais  
3. Revalidar pareamento  
4. Ativar MFA  

## Lições Aprendidas
- API não deve expor endpoints críticos  

## Recomendações
- Alertas para comandos críticos  
